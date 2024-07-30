import asyncio


class AsyncDatabase:
    async def query(self, sql):
        print(f"Executing query: {sql}")
        await asyncio.sleep(1)  # Simulate a database I/O operation
        return f"Results for query: {sql}"


class SyncFacade:
    def __init__(self):
        self._db = AsyncDatabase()
        self._loop = asyncio.get_event_loop()

    def query(self, sql):
        return self._loop.run_until_complete(self._db.query(sql))


# Usage example
if __name__ == "__main__":
    db = SyncFacade()
    result = db.query("SELECT * FROM users")
    print(result)
