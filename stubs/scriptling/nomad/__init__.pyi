"""
Scriptling Nomad Library - Type stubs for IntelliSense support.

HashiCorp Nomad client covering CSI volumes and jobs. All operations go
through a NomadClient obtained from Client().
"""

def Client(addr: str, *, token: str = "", insecure: bool = False, timeout: float = 10) -> "NomadClient":
    """
    Create a Nomad client.

    Parameters:
        addr (str): Nomad HTTP API address, e.g. "http://127.0.0.1:4646"
        token (str, optional): ACL token, sent as the X-Nomad-Token header. Default: ""
        insecure (bool, optional): Skip TLS certificate verification. Default: False
        timeout (float, optional): Per-request HTTP timeout in seconds. Default: 10

    Returns:
        NomadClient: A client instance

    Example:
        import scriptling.nomad as nomad

        c = nomad.Client("https://nomad.example.com:4646", token="secret")
        c = nomad.Client("https://nomad.example.com:4646", token="secret", timeout=5)
    """
    ...

class NomadClient:
    """
    Client for a Nomad cluster's HTTP API.

    Obtain an instance via nomad.Client(addr, token=...).
    """

    def csi_volumes_list(self, *, namespace: str = "*", plugin_id: str = "") -> list[dict]:
        """
        List CSI volumes.

        Parameters:
            namespace (str, optional): Namespace to list, "*" for all namespaces. Default: "*"
            plugin_id (str, optional): Filter by CSI plugin ID. Default: "" (no filter)

        Returns:
            list[dict]: List of volume summary dicts, each with:
                - id (str): Volume ID
                - name (str): Volume name
                - namespace (str): Namespace
                - plugin_id (str): CSI plugin ID
                - provider (str): CSI provider name
                - schedulable (bool): Whether the volume can currently be scheduled
                - controllers_healthy (int): Number of healthy controller plugins
                - nodes_healthy (int): Number of healthy node plugins

        Example:
            for v in c.csi_volumes_list(plugin_id="ceph-csi"):
                if v["id"].startswith("qaannon") or v["id"].startswith("qaprod"):
                    print(v["id"])
        """
        ...

    def csi_volume_get(self, id: str, *, namespace: str = "") -> dict:
        """
        Get details for a CSI volume.

        Parameters:
            id (str): Volume ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Returns:
            dict: Full volume specification and status, as returned by the Nomad API

        Example:
            vol = c.csi_volume_get("qaprod-data-01")
            print(vol["Provider"])
        """
        ...

    def csi_volume_register(self, id: str, volume: dict, *, namespace: str = "") -> None:
        """
        Register a pre-existing CSI volume with Nomad.

        The backing storage must already exist on the storage provider. Use
        csi_volume_create() instead to have the CSI plugin provision new storage.

        Parameters:
            id (str): Volume ID
            volume (dict): Volume specification in Nomad's CSI volume JSON format
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Example:
            c.csi_volume_register("qaprod-data-01", {
                "Name": "qaprod-data-01",
                "PluginID": "ceph-csi",
                "Capacity": 10 * 1024 * 1024 * 1024,
                "AccessMode": "single-node-writer",
                "AttachmentMode": "file-system",
            })
        """
        ...

    def csi_volume_create(self, id: str, volume: dict, *, namespace: str = "") -> None:
        """
        Create a CSI volume and provision backing storage.

        Instructs the CSI controller plugin to provision new backing storage
        (e.g. a Ceph RBD image) and registers the volume in Nomad. Use
        csi_volume_register() instead if the backing storage already exists.

        Parameters:
            id (str): Volume ID
            volume (dict): Volume specification in Nomad's CSI volume JSON format
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Example:
            c.csi_volume_create("qaprod-data-01", {
                "Name": "qaprod-data-01",
                "PluginID": "ceph-csi",
                "RequestedCapacityMin": 10 * 1024 * 1024 * 1024,
                "RequestedCapabilities": [{"AccessMode": "single-node-writer", "AttachmentMode": "file-system"}],
            }, namespace="fortixqa")
        """
        ...

    def csi_volume_deregister(self, id: str, *, namespace: str = "", force: bool = False) -> None:
        """
        Deregister a CSI volume from Nomad without removing the backing storage.

        The underlying data (e.g. Ceph RBD image) remains intact. Use
        csi_volume_delete() to also remove the backing storage.

        Parameters:
            id (str): Volume ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)
            force (bool, optional): Force detach any remaining claims first. Default: False

        Example:
            c.csi_volume_deregister("qaprod-orphaned-01", force=True)
        """
        ...

    def csi_volume_delete(self, id: str, *, namespace: str = "") -> None:
        """
        Delete a CSI volume and its backing storage.

        Instructs the CSI controller plugin to destroy the backing storage
        (e.g. Ceph RBD image) and then deregisters the volume from Nomad.
        This permanently removes the data.

        Parameters:
            id (str): Volume ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Example:
            c.csi_volume_delete("qaprod-orphaned-01", namespace="fortixqa")
        """
        ...

    def host_volumes_list(self, *, namespace: str = "*", node_id: str = "", node_pool: str = "", plugin_id: str = "") -> list[dict]:
        """
        List dynamic host volumes.

        Parameters:
            namespace (str, optional): Namespace to list, "*" for all namespaces. Default: "*"
            node_id (str, optional): Filter by node ID. Default: "" (no filter)
            node_pool (str, optional): Filter by node pool. Default: "" (no filter)
            plugin_id (str, optional): Filter by host volume plugin ID. Default: "" (no filter)

        Returns:
            list[dict]: List of volume summary dicts, each with:
                - id (str): Volume ID
                - name (str): Volume name
                - namespace (str): Namespace
                - plugin_id (str): Host volume plugin ID
                - node_id (str): Node the volume is on
                - node_pool (str): Node pool
                - state (str): Volume state

        Example:
            for v in c.host_volumes_list():
                print(v["name"], v["node_id"], v["state"])
        """
        ...

    def host_volume_get(self, id: str, *, namespace: str = "") -> dict:
        """
        Get details for a dynamic host volume.

        Parameters:
            id (str): Volume ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Returns:
            dict: Full volume specification and status, as returned by the Nomad API

        Example:
            vol = c.host_volume_get("abc123-def456")
            print(vol["Name"], vol["HostPath"], vol["State"])
        """
        ...

    def host_volume_register(self, id: str, volume: dict, *, namespace: str = "") -> None:
        """
        Register a pre-existing dynamic host volume with Nomad.

        The backing storage (e.g. a pre-mounted NFS or CephFS path) must
        already exist on the node. Use host_volume_create() instead to have
        the host volume plugin provision storage.

        Parameters:
            id (str): Volume ID
            volume (dict): Volume specification in Nomad's host volume JSON format
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Example:
            c.host_volume_register("vol-abc123", {
                "Name": "cephfs-code",
                "PluginID": "mkdir",
                "NodeID": "node-1",
                "HostPath": "/cephfs/sys-code/Freedom3",
                "Capacity": 100 * 1024 * 1024 * 1024,
                "RequestedCapabilities": [{"AccessMode": "single-node-writer", "AttachmentMode": "file-system"}],
            })
        """
        ...

    def host_volume_create(self, id: str, volume: dict, *, namespace: str = "") -> None:
        """
        Create a dynamic host volume via a plugin.

        Instructs the host volume plugin to provision storage on the target
        node and registers the resulting volume in Nomad. Use
        host_volume_register() instead if the backing storage already exists.

        Parameters:
            id (str): Volume ID
            volume (dict): Volume specification in Nomad's host volume JSON format
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Example:
            c.host_volume_create("vol-new-01", {
                "Name": "app-data",
                "PluginID": "mkdir",
                "NodePool": "production",
                "RequestedCapacityMinBytes": 50 * 1024 * 1024 * 1024,
                "RequestedCapabilities": [{"AccessMode": "single-node-writer", "AttachmentMode": "file-system"}],
                "Parameters": {"path": "/opt/volumes/app-data"},
            })
        """
        ...

    def host_volume_delete(self, id: str, *, namespace: str = "") -> None:
        """
        Delete a dynamic host volume.

        Instructs the host volume plugin to destroy the backing storage on
        the node and deregisters the volume from Nomad.

        Parameters:
            id (str): Volume ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Example:
            c.host_volume_delete("vol-abc123", namespace="production")
        """
        ...

    def jobs_list(self, *, namespace: str = "*", prefix: str = "") -> list[dict]:
        """
        List jobs.

        Parameters:
            namespace (str, optional): Namespace to list, "*" for all namespaces. Default: "*"
            prefix (str, optional): Filter by job ID prefix. Default: "" (no filter)

        Returns:
            list[dict]: List of job summary dicts, each with:
                - id (str): Job ID
                - name (str): Job name
                - namespace (str): Namespace
                - type (str): Job type e.g. "service", "batch", "system"
                - status (str): Current status e.g. "running", "pending", "dead"
                - priority (int): Job priority

        Example:
            for j in c.jobs_list(prefix="qaannon"):
                print(j["id"], j["status"])
        """
        ...

    def job_get(self, id: str, *, namespace: str = "") -> dict:
        """
        Get the full specification and status for a job.

        Parameters:
            id (str): Job ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)

        Returns:
            dict: Job specification and status, as returned by the Nomad API

        Example:
            job = c.job_get("qaprod-api")
            print(job["Status"])
        """
        ...

    def job_register(self, job: dict) -> dict:
        """
        Register (create or update) a job.

        Parameters:
            job (dict): Job specification in Nomad's JSON job format (e.g. from
                        jobs_parse() or job_get()["Job"])

        Returns:
            dict: Registration response with keys:
                - EvalID (str): Evaluation ID created for this registration
                - EvalCreateIndex (int)
                - JobModifyIndex (int)
                - Warnings (str)

        Example:
            parsed = c.jobs_parse(hcl_text)
            result = c.job_register(parsed)
            print(result["EvalID"])
        """
        ...

    def job_stop(self, id: str, *, namespace: str = "", purge: bool = False) -> dict:
        """
        Stop a job.

        Parameters:
            id (str): Job ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)
            purge (bool, optional): Fully remove the job from Nomad's state
                                    instead of leaving it stopped. Default: False

        Returns:
            dict: Stop response with keys: EvalID (str), EvalCreateIndex (int),
                  JobModifyIndex (int)

        Example:
            c.job_stop("qaprod-old-job", purge=True)
        """
        ...

    def wait_job_stopped(self, id: str, *, namespace: str = "", timeout: int = 30) -> bool:
        """
        Wait for a job to reach the "dead" status.

        Parameters:
            id (str): Job ID
            namespace (str, optional): Namespace. Default: "" (Nomad default namespace)
            timeout (int, optional): Maximum time to wait in seconds. Default: 30

        Returns:
            bool: True if the job is stopped, False if the timeout was reached

        Example:
            c.job_stop("qaprod-old-job")
            if not c.wait_job_stopped("qaprod-old-job", timeout=60):
                print("job did not stop in time")
        """
        ...

    def job_validate(self, job: dict) -> dict:
        """
        Validate a job specification without submitting it.

        Parameters:
            job (dict): Job specification in Nomad's JSON job format

        Returns:
            dict: Validation result with keys: DriverConfigValidated (bool),
                  ValidationErrors (list[str]), Warnings (str)

        Example:
            result = c.job_validate(parsed_job)
            if result["ValidationErrors"]:
                print(result["ValidationErrors"])
        """
        ...

    def job_plan(self, id: str, job: dict, *, diff: bool = False) -> dict:
        """
        Dry-run a job registration and return the resulting scheduler plan.

        Parameters:
            id (str): Job ID
            job (dict): Job specification in Nomad's JSON job format
            diff (bool, optional): Include a diff against the current job
                                   version. Default: False

        Returns:
            dict: Plan result with keys such as JobModifyIndex (int),
                  Annotations (dict), FailedTGAllocs (dict)

        Example:
            plan = c.job_plan("qaprod-api", parsed_job, diff=True)
        """
        ...

    def jobs_parse(self, hcl: str, *, canonicalize: bool = False) -> dict:
        """
        Convert an HCL job specification into Nomad's JSON job format.

        Parameters:
            hcl (str): Job specification in HCL format
            canonicalize (bool, optional): Fill in default values for optional
                                           fields. Default: False

        Returns:
            dict: Job specification in Nomad's JSON job format, suitable for
                  job_register(), job_validate(), or job_plan()

        Example:
            parsed = c.jobs_parse(open("job.nomad.hcl").read())
            c.job_register(parsed)
        """
        ...
