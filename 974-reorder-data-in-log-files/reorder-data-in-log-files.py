class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def hasnum(log):
            return any(char.isdigit() for char in log)
        
        letter_log, digit_log = [],[]
        for i, log in enumerate(logs):
            vals = log.split(" ")
            
            if hasnum(vals[1:]):
                digit_log.append(log)
            else:
                letter_log.append([' '.join(vals[1:]), vals[0], i])
            
        res = []
        for log in sorted(letter_log):
            res.append(logs[log[2]])

        return res + digit_log
