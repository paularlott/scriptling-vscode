"""
Scriptling Container Library - Type stubs for IntelliSense support.

Container lifecycle management for Docker, Podman, and Apple Containers.
All operations go through a ContainerClient obtained from Client().
"""

from typing import Optional

def runtimes() -> list[str]:
    """
    List available container runtimes.

    Probes each supported runtime and returns the names of those that are
    currently installed and running on this system.

    Returns:
        list[str]: Subset of ["docker", "podman", "apple"]

    Example:
        import scriptling.container as container

        available = container.runtimes()
        print("Available runtimes:", available)
    """
    ...

def Client(driver: str, *, socket: str = "") -> "ContainerClient":
    """
    Create a container client for the specified runtime driver.

    Parameters:
        driver (str): Runtime to use — "docker", "podman", or "apple"
        socket (str, optional): Override the endpoint. Accepts:
            - Unix socket path:  /var/run/docker.sock
            - Unix socket URI:   unix:///var/run/docker.sock
            - TCP (Docker only): tcp://192.168.1.10:2375 or 192.168.1.10:2375
            - TLS (Docker only): https://192.168.1.10:2376
            Defaults to DOCKER_HOST / CONTAINER_HOST env vars (via --docker-sock / --podman-sock CLI flags),
            then /var/run/docker.sock or /var/run/podman.sock.

    Returns:
        ContainerClient: A client instance

    Example:
        import scriptling.container as container

        c = container.Client("docker")
        c = container.Client("docker", socket="unix:///Users/paul/.lima/docker/sock/docker.sock")
        c = container.Client("docker", socket="tcp://192.168.1.10:2375")
        c = container.Client("podman")
        c = container.Client("podman", socket="unix:///run/user/1000/podman/podman.sock")
        c = container.Client("apple")
    """
    ...

class ContainerClient:
    """
    Client for managing containers on a specific runtime.

    Obtain an instance via container.Client(driver).
    """

    def driver(self) -> str:
        """
        Return the name of the active runtime driver.

        Returns:
            str: "docker", "podman", or "apple"
        """
        ...

    def image_list(self) -> list[dict]:
        """
        List locally available images.

        Returns:
            list[dict]: List of image info dicts, each with:
                - id (str): Image ID (digest for Apple, full ID for Docker/Podman)
                - reference (str): Image reference e.g. "ubuntu:24.04"
                - digest (str): Content digest e.g. "sha256:abc123..."
                - size (int): Manifest size in bytes

        Example:
            for img in c.image_list():
                print(img["reference"], img["digest"])
        """
        ...

    def image_pull(self, image: str) -> None:
        """
        Pull an image from a registry.

        Parameters:
            image (str): Image reference e.g. "ubuntu:24.04"

        Example:
            c.image_pull("ubuntu:24.04")
        """
        ...

    def image_remove(self, image: str) -> None:
        """
        Remove a local image.

        Parameters:
            image (str): Image reference e.g. "nginx:latest"

        Example:
            c.image_remove("ubuntu:24.04")
        """
        ...

    def exec(
        self,
        name_or_id: str,
        command: list[str],
        *,
        env: list[str] = [],
        workdir: str = "",
        user: str = "",
    ) -> dict:
        """
        Run a command in a running container and capture output.

        Parameters:
            name_or_id (str): Container name or ID
            command (list[str]): Command and arguments e.g. ["/bin/sh", "-c", "echo hi"]
            env (list[str], optional): Environment variables e.g. ["KEY=value"]
            workdir (str, optional): Working directory inside the container
            user (str, optional): User to run as e.g. "root" or "1000:1000"

        Returns:
            dict: Result with keys:
                - stdout (str): Captured standard output
                - stderr (str): Captured standard error
                - exit_code (int): Process exit code

        Example:
            result = c.exec("app", ["/bin/sh", "-c", "cat /etc/os-release"])
            print(result["stdout"])
            print("exit:", result["exit_code"])
        """
        ...

    def exec_stream(
        self,
        name_or_id: str,
        command: list[str],
        callback,
        *,
        env: list[str] = [],
        workdir: str = "",
        user: str = "",
    ) -> dict:
        """
        Run a command in a running container and stream output line by line.

        Calls callback(stream, line) for each line of output as it arrives.
        stream is "stdout" or "stderr".

        Parameters:
            name_or_id (str): Container name or ID
            command (list[str]): Command and arguments
            callback (callable): Function called with (stream, line) for each output line
            env (list[str], optional): Environment variables e.g. ["KEY=value"]
            workdir (str, optional): Working directory inside the container
            user (str, optional): User to run as e.g. "root" or "1000:1000"

        Returns:
            dict: Result with exit_code (int). stdout and stderr are empty strings.

        Example:
            def on_line(stream, line):
                print(f"[{stream}] {line}")

            result = c.exec_stream("app", ["/bin/sh", "-c", "for i in 1 2 3; do echo $i; done"], on_line)
            print("exit:", result["exit_code"])
        """
        ...

    def run(
        self,
        image: str,
        *,
        name: str = "",
        ports: list[str] = [],
        env: list[str] = [],
        volumes: list[str] = [],
        command: list[str] = [],
        network: str = "",
        privileged: bool = False,
    ) -> str:
        """
        Create and start a container.

        Parameters:
            image (str): Image reference e.g. "ubuntu:24.04"
            name (str, optional): Container name
            ports (list[str], optional): Port mappings e.g. ["8080:80"]
            env (list[str], optional): Environment variables e.g. ["KEY=value"]
            volumes (list[str], optional): Volume mounts e.g. ["mydata:/data"]
            command (list[str], optional): Override command e.g. ["/bin/sh", "-c", "echo hi"]
            network (str, optional): Network name
            privileged (bool, optional): Run privileged (default False)

        Returns:
            str: Container ID

        Example:
            id = c.run("ubuntu:24.04", name="app", env=["DEBUG=1"], volumes=["data:/data"])
        """
        ...

    def stop(self, name_or_id: str) -> None:
        """
        Stop a running container.

        Parameters:
            name_or_id (str): Container name or ID

        Example:
            c.stop("app")
        """
        ...

    def remove(self, name_or_id: str) -> None:
        """
        Remove a stopped container.

        Parameters:
            name_or_id (str): Container name or ID

        Example:
            c.remove("app")
        """
        ...

    def inspect(self, name_or_id: str) -> dict:
        """
        Get container details.

        Parameters:
            name_or_id (str): Container name or ID

        Returns:
            dict: Container info with keys:
                - id (str): Container ID
                - name (str): Container name
                - status (str): Current status e.g. "running", "exited"
                - image (str): Image reference
                - running (bool): True if the container is currently running

        Example:
            info = c.inspect("app")
            print(info["status"])
        """
        ...

    def list(self) -> list[dict]:
        """
        List all containers (running and stopped).

        Returns:
            list[dict]: List of container info dicts, each with:
                - id (str): Container ID
                - name (str): Container name
                - status (str): Current status
                - image (str): Image reference
                - running (bool): True if currently running

        Example:
            for item in c.list():
                print(item["name"], item["status"])
        """
        ...

    def volume_create(self, name: str) -> None:
        """
        Create a named volume.

        Parameters:
            name (str): Volume name

        Example:
            c.volume_create("mydata")
        """
        ...

    def volume_remove(self, name: str) -> None:
        """
        Remove a named volume.

        Parameters:
            name (str): Volume name

        Example:
            c.volume_remove("mydata")
        """
        ...

    def volume_list(self) -> list[str]:
        """
        List named volumes.

        Returns:
            list[str]: Volume names

        Example:
            for v in c.volume_list():
                print(v)
        """
        ...
