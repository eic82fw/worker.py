from workers import WorkerEntrypoint, Response


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return Response(
            "Hello from Python + Cloudflare 🚀",
            headers={"content-type": "text/plain"}
        )
