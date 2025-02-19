def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    
    # O(n) complexity since we are iterating through the intervals and checking if the new interval can be inserted concluding once the insertion and any merging is complete.
    
    mod_intervals = []
    lower = new_interval[0]
    upper = new_interval[1]
    
    for interval_idx, interval in enumerate(intervals):
        if upper < interval[0]:
            mod_intervals.append([lower, upper])
            return mod_intervals + intervals[interval_idx:]
        elif lower > interval[1]:
            mod_intervals.append(interval)
        else:
            lower = min(lower, interval[0])
            upper = max(upper, interval[1])
            
    mod_intervals.append([lower, upper])
    return mod_intervals
                
if __name__ == "__main__":
    
    mod_interval = insert([[1,2],[3,5],[6,7],[8,10],[12,16]], new_interval = [4,8])
    print(mod_interval)