class Solution:
    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    # Total Time: 15 m + prev tries
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = [False for _ in range(len(transactions))]
        names, times, prices, cities = [], [], [], []
        for trans in transactions:
            n, t, p, c = trans.split(',')
            names.append(n), times.append(int(t)), prices.append(int(p)), cities.append(c)
        for i in range(len(transactions)):
            if prices[i] > 1000:
                invalid[i] = True
            for j in range(i+1, len(transactions)):
                if names[i] == names[j] and abs(times[j] - times[i]) <= 60 and cities[j] != cities[i]:
                    invalid[i], invalid[j] = True, True
        result = []
        for i in range(len(invalid)):
            if invalid[i]:
                result.append(transactions[i])
        return result