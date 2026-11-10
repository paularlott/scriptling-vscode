"""
Scriptling Provision Library - Type stubs for IntelliSense support.

Provisioning libraries for setting up a machine: idempotent file operations,
fetching remote artifacts, running commands and installing packages, as the
script's user or, with become=True, as root.

Sub-libraries:
  - provision.file: Ensure files, directories, and managed blocks
  - provision.fetch: Fetch HTTP/HTTPS files and optionally unpack ZIP archives
  - provision.command: Run commands, as the user or as root
  - provision.package: Install and remove packages with apt, dnf, yum, apk or brew
"""
