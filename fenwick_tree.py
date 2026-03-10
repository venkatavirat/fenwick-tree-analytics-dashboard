# Fenwick Tree implementation for sales data analytics
# Handles 100K+ records with O(log n) updates/queries

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)
    
    def update(self, idx, val):
        idx += 1  # 1-indexed
        while idx <= self.size:
            self.tree[idx] += val
            idx += idx & -idx  # least significant bit
    
    def query(self, idx):
        idx += 1
        total = 0
        while idx > 0:
            total += self.tree[idx]
            idx -= idx & -idx
        return total

# Testing with sample sales data
if __name__ == "__main__":
    ft = FenwickTree(12)
    sales = [2,1,1,3,2,3,4,5,6,7,8,9]
    
    for i, sale in enumerate(sales):
        ft.update(i, sale)
    
    print(f"Total sales first 6 days: {ft.query(5)}")  # Should be 12
