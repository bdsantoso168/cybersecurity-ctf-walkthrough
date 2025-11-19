#!/usr/bin/env python3
"""
Password Strength Analyzer
Analyzes password strength and provides security recommendations
"""

import re
import sys
import math
from typing import Dict, List

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = {
            'password', '123456', '12345678', 'qwerty', 'abc123',
            'monkey', 'letmein', 'trustno1', 'dragon', 'baseball',
            'iloveyou', 'master', 'sunshine', 'ashley', 'bailey',
            'shadow', 'superman', 'password1', 'password123'
        }
    
    def analyze_password(self, password: str) -> Dict:
        """Comprehensive password analysis"""
        
        analysis = {
            'password': password,
            'length': len(password),
            'has_lowercase': bool(re.search(r'[a-z]', password)),
            'has_uppercase': bool(re.search(r'[A-Z]', password)),
            'has_digits': bool(re.search(r'\\d', password)),
            'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password)),
            'is_common': password.lower() in self.common_passwords,
            'has_sequence': self.has_sequence(password),
            'has_repetition': self.has_repetition(password),
            'entropy': self.calculate_entropy(password),
            'charset_size': self.get_charset_size(password),
            'crack_time': None,
            'strength': None,
            'score': 0
        }
        
        # Calculate score
        analysis['score'] = self.calculate_score(analysis)
        
        # Determine strength
        analysis['strength'] = self.determine_strength(analysis['score'])
        
        # Estimate crack time
        analysis['crack_time'] = self.estimate_crack_time(analysis)
        
        return analysis
    
    def has_sequence(self, password: str) -> bool:
        """Check for sequential characters"""
        sequences = ['abc', '123', 'qwe', 'asd', 'zxc']
        password_lower = password.lower()
        
        for seq in sequences:
            if seq in password_lower:
                return True
        
        # Check for ascending/descending numbers
        for i in range(len(password) - 2):
            if password[i:i+3].isdigit():
                nums = [int(password[i]), int(password[i+1]), int(password[i+2])]
                if nums[1] - nums[0] == 1 and nums[2] - nums[1] == 1:
                    return True
                if nums[0] - nums[1] == 1 and nums[1] - nums[2] == 1:
                    return True
        
        return False
    
    def has_repetition(self, password: str) -> bool:
        """Check for repeated characters"""
        for i in range(len(password) - 2):
            if password[i] == password[i+1] == password[i+2]:
                return True
        return False
    
    def get_charset_size(self, password: str) -> int:
        """Calculate character set size"""
        charset = 0
        
        if re.search(r'[a-z]', password):
            charset += 26
        if re.search(r'[A-Z]', password):
            charset += 26
        if re.search(r'\\d', password):
            charset += 10
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            charset += 32
        
        return charset
    
    def calculate_entropy(self, password: str) -> float:
        """Calculate password entropy (bits)"""
        charset_size = self.get_charset_size(password)
        if charset_size == 0:
            return 0
        
        entropy = len(password) * math.log2(charset_size)
        return round(entropy, 2)
    
    def calculate_score(self, analysis: Dict) -> int:
        """Calculate password strength score (0-100)"""
        score = 0
        
        # Length scoring (up to 30 points)
        length = analysis['length']
        if length >= 16:
            score += 30
        elif length >= 12:
            score += 25
        elif length >= 8:
            score += 20
        elif length >= 6:
            score += 10
        else:
            score += 5
        
        # Character variety (up to 40 points)
        if analysis['has_lowercase']:
            score += 10
        if analysis['has_uppercase']:
            score += 10
        if analysis['has_digits']:
            score += 10
        if analysis['has_special']:
            score += 10
        
        # Entropy bonus (up to 20 points)
        entropy = analysis['entropy']
        if entropy >= 80:
            score += 20
        elif entropy >= 60:
            score += 15
        elif entropy >= 40:
            score += 10
        elif entropy >= 20:
            score += 5
        
        # Penalties
        if analysis['is_common']:
            score -= 40
        if analysis['has_sequence']:
            score -= 15
        if analysis['has_repetition']:
            score -= 10
        
        # Ensure score is between 0 and 100
        return max(0, min(100, score))
    
    def determine_strength(self, score: int) -> str:
        """Determine password strength category"""
        if score >= 80:
            return "VERY STRONG"
        elif score >= 60:
            return "STRONG"
        elif score >= 40:
            return "MODERATE"
        elif score >= 20:
            return "WEAK"
        else:
            return "VERY WEAK"
    
    def estimate_crack_time(self, analysis: Dict) -> str:
        """Estimate time to crack password"""
        charset = analysis['charset_size']
        length = analysis['length']
        
        if charset == 0:
            return "Instant"
        
        # Assume 1 billion guesses per second
        guesses_per_second = 1_000_000_000
        
        # Total possible combinations
        combinations = charset ** length
        
        # Time in seconds
        seconds = combinations / guesses_per_second
        
        # Convert to human-readable time
        if seconds < 1:
            return "Instant"
        elif seconds < 60:
            return f"{int(seconds)} seconds"
        elif seconds < 3600:
            return f"{int(seconds / 60)} minutes"
        elif seconds < 86400:
            return f"{int(seconds / 3600)} hours"
        elif seconds < 31536000:
            return f"{int(seconds / 86400)} days"
        elif seconds < 31536000 * 1000:
            return f"{int(seconds / 31536000)} years"
        else:
            return "Centuries"
    
    def get_recommendations(self, analysis: Dict) -> List[str]:
        """Get recommendations for improving password"""
        recommendations = []
        
        if analysis['length'] < 12:
            recommendations.append("• Increase length to at least 12 characters")
        
        if not analysis['has_lowercase']:
            recommendations.append("• Add lowercase letters (a-z)")
        
        if not analysis['has_uppercase']:
            recommendations.append("• Add uppercase letters (A-Z)")
        
        if not analysis['has_digits']:
            recommendations.append("• Add numbers (0-9)")
        
        if not analysis['has_special']:
            recommendations.append("• Add special characters (!@#$%^&*)")
        
        if analysis['is_common']:
            recommendations.append("• Avoid common passwords")
        
        if analysis['has_sequence']:
            recommendations.append("• Avoid sequential characters (abc, 123)")
        
        if analysis['has_repetition']:
            recommendations.append("• Avoid repeated characters (aaa, 111)")
        
        if not recommendations:
            recommendations.append("• Password is strong! Consider using a password manager")
        
        return recommendations
    
    def print_analysis(self, analysis: Dict):
        """Print detailed password analysis"""
        
        print("\\n" + "="*70)
        print("  PASSWORD STRENGTH ANALYSIS")
        print("="*70)
        
        # Basic info
        print(f"\\nPassword: {'*' * len(analysis['password'])}")
        print(f"Length:   {analysis['length']} characters")
        
        # Character types
        print("\\nCharacter Types:")
        print(f"  Lowercase: {'✓' if analysis['has_lowercase'] else '✗'}")
        print(f"  Uppercase: {'✓' if analysis['has_uppercase'] else '✗'}")
        print(f"  Digits:    {'✓' if analysis['has_digits'] else '✗'}")
        print(f"  Special:   {'✓' if analysis['has_special'] else '✗'}")
        
        # Security metrics
        print("\\nSecurity Metrics:")
        print(f"  Charset Size: {analysis['charset_size']} characters")
        print(f"  Entropy:      {analysis['entropy']} bits")
        print(f"  Common:       {'Yes ⚠' if analysis['is_common'] else 'No ✓'}")
        print(f"  Sequence:     {'Yes ⚠' if analysis['has_sequence'] else 'No ✓'}")
        print(f"  Repetition:   {'Yes ⚠' if analysis['has_repetition'] else 'No ✓'}")
        
        # Strength assessment
        print("\\n" + "-"*70)
        print(f"STRENGTH:    {analysis['strength']}")
        print(f"SCORE:       {analysis['score']}/100")
        print(f"CRACK TIME:  {analysis['crack_time']}")
        print("-"*70)
        
        # Recommendations
        print("\\nRECOMMENDATIONS:")
        recommendations = self.get_recommendations(analysis)
        for rec in recommendations:
            print(rec)
        
        print("\\n" + "="*70 + "\\n")

def main():
    print("""
╔═══════════════════════════════════════════════════════════╗
║       PASSWORD STRENGTH ANALYZER - Competition Tool       ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter password to analyze: ")
    
    analyzer = PasswordAnalyzer()
    analysis = analyzer.analyze_password(password)
    analyzer.print_analysis(analysis)

if __name__ == "__main__":
    main()
