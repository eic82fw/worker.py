from workers import WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response(
            "Hello from Python on Cloudflare!",
            headers={"content-type": "text/plain"}
        )
