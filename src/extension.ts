import * as vscode from 'vscode';
import * as path from 'path';

let stubPathDisposable: vscode.Disposable | undefined;

export function activate(context: vscode.ExtensionContext) {
    // Configure Python extension to use our bundled stubs
    configurePythonStubs(context);

    // Listen for configuration changes
    context.subscriptions.push(
        vscode.workspace.onDidChangeConfiguration(e => {
            if (e.affectsConfiguration('scriptling.stubPath')) {
                configurePythonStubs(context);
            }
        })
    );

    console.log('Scriptling extension activated');
}

export function deactivate() {
    if (stubPathDisposable) {
        stubPathDisposable.dispose();
    }
}

function configurePythonStubs(context: vscode.ExtensionContext) {
    // Get the path to bundled stubs
    const bundledStubPath = path.join(context.extensionPath, 'stubs');

    // Check if user has specified a custom stub path
    const config = vscode.workspace.getConfiguration('scriptling');
    const customStubPath = config.get<string>('stubPath', '');

    // Determine which stub path to use
    const stubPath = customStubPath || bundledStubPath;

    // Update Python analysis settings
    const pythonConfig = vscode.workspace.getConfiguration('python.analysis');

    // Get existing extraPaths and add our stub path
    const existingPaths = pythonConfig.get<string[]>('extraPaths', []);
    const paths = new Set(existingPaths);

    // Add our stub path if not already present
    if (!paths.has(stubPath)) {
        paths.add(stubPath);
        pythonConfig.update('extraPaths', Array.from(paths), vscode.ConfigurationTarget.Global);
    }

    // Also configure typeStubPaths if available
    const typeStubPaths = pythonConfig.get<string[]>('typeStubPaths', []);
    const typePaths = new Set(typeStubPaths);
    if (!typePaths.has(stubPath)) {
        typePaths.add(stubPath);
        pythonConfig.update('typeStubPaths', Array.from(typePaths), vscode.ConfigurationTarget.Global);
    }

    vscode.window.showInformationMessage(
        `Scriptling: Configured IntelliSense stubs from ${path.basename(stubPath)}`
    );
}
