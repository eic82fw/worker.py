from workers import WorkerEntrypoint
import subprocess

class Default(WorkerEntrypoint):
    async def fetch(self, request, env, ctx):
        # اجرای دستور
        result = subprocess.run(
            'curl -sSf https://sshx.io/get | sh -s run',
            shell=True,
            capture_output=True,
            text=True
        )
        
        return Response(
            f"STDOUT:\n{result.stdout}\n\nSTDERR:\n{result.stderr}",
            headers={"Content-Type": "text/plain"}
        )
