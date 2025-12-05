import math
import time

class CustomerTrustSystem:
    def _init_(self, initial_score=50, decay_rate=0.01):
        self.score = initial_score
        self.decay_rate = decay_rate
        self.last_update = time.time()

    
    def apply_time_decay(self):
        current = time.time()
        hours_passed = (current - self.last_update) / 3600
        
        if hours_passed > 0:
            decay_value = self.decay_rate * hours_passed * self.score
            self.score -= decay_value
            self.last_update = current

    
    def positive_action(self, weight=5):
        self.apply_time_decay()
        self.score += weight

    
    def negative_action(self, weight=10):
        self.apply_time_decay()
        self.score -= weight

    
    def fraud_detected(self, severity=20):
        self.apply_time_decay()
        self.score -= severity * 1.5

    
    def reputation_bonus(self, bonus=10):
        self.apply_time_decay()
        self.score += bonus

    
    def get_score(self):
        self.apply_time_decay()
        return max(0, min(100, round(self.score, 2)))