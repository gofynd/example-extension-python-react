class ExtensionHandlers():

    async def install(self, request):
        pass

    async def auth(self, request):
        # Writee you code here to return initial launch url after suth process complete
        company_id = int(request.args.get("company_id"))
        return f"{request.conn_info.ctx.extension.base_url}/company/{company_id}"

    async def uninstall(self, request):
        # Write your code here to cleanup data related to extension
        # If task is time taking then process it async on other process.
        pass