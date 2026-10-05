class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] 

        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        result = ""

        # if you didn't find the `key` for example "foo", return an empty list []
        values = self.store.get(key, [])

        left = 0
        right = len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                result = values[mid][0]

                left = mid + 1

            else:
                right = mid - 1

        return result       




        
