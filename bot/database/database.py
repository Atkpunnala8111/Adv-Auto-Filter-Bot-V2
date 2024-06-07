
        A Funtion to count total filters of a group
        """
        return await self.fcol.count_documents({"group_id": group_id})


