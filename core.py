# core.py
import csv
from statistics import mean

class StudentAnalyzer:
    def __init__(self, filename):
        self.students = self.load_data(filename)
        
    def load_data(self, filename):
        """Load student data from CSV file"""
        students = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert string values to appropriate types
                student = {
                    'student_id': int(row['Student_ID']),
                    'study_hours': float(row['Study_Hours_Per_Day']),
                    'sleep_hours': float(row['Sleep_Hours_Per_Day']),
                    'physical_hours': float(row['Physical_Activity_Hours_Per_Day']),
                    'stress_level': row['Stress_Level'],
                    'cgpa': float(row['GPA'])
                }
                students.append(student)
        return students
    
    def get_average_cgpa(self):
        """Calculate average CGPA"""
        cgpas = [student['cgpa'] for student in self.students]
        return round(mean(cgpas), 2)
    
    def get_study_impact(self):
        """Group students by study hours and show average CGPA"""
        # Group students by study hour ranges
        groups = {'0-2': [], '2-4': [], '4-6': [], '6+': []}
        
        for student in self.students:
            hours = student['study_hours']
            if hours <= 2:
                groups['0-2'].append(student['cgpa'])
            elif hours <= 4:
                groups['2-4'].append(student['cgpa'])
            elif hours <= 6:
                groups['4-6'].append(student['cgpa'])
            else:
                groups['6+'].append(student['cgpa'])
        
        # Calculate averages for each group
        results = {}
        for range_name, cgpas in groups.items():
            if cgpas:  # Only include ranges that have students
                results[range_name] = round(mean(cgpas), 2)
        
        return results
    
    def get_stress_impact(self):
        """Group students by stress level and show average CGPA"""
        # Group CGPAs by stress level
        stress_groups = {}
        
        for student in self.students:
            level = student['stress_level']
            if level not in stress_groups:
                stress_groups[level] = []
            stress_groups[level].append(student['cgpa'])
        
        # Calculate average CGPA for each stress level
        results = {}
        for level in sorted(stress_groups.keys()):
            results[level] = round(mean(stress_groups[level]), 2)
        
        return results
    
    def find_top_performers(self, count=10):
        """Get top performing students and their habits"""
        # Sort students by CGPA
        sorted_students = sorted(self.students, 
                               key=lambda x: x['cgpa'], 
                               reverse=True)
        
        # Get top students
        top_students = sorted_students[:count]
        
        # Calculate their average habits
        habits = {
            'study_hours': round(mean(s['study_hours'] for s in top_students), 2),
            'sleep_hours': round(mean(s['sleep_hours'] for s in top_students), 2),
            'physical_hours': round(mean(s['physical_hours'] for s in top_students), 2),
            'average_cgpa': round(mean(s['cgpa'] for s in top_students), 2)
        }
        
        return habits
    
    def get_basic_stats(self):
        """Get basic statistics about the dataset"""
        return {
            'total_students': len(self.students),
            'average_cgpa': self.get_average_cgpa(),
            'average_study_hours': round(mean(s['study_hours'] for s in self.students), 2),
            'average_sleep_hours': round(mean(s['sleep_hours'] for s in self.students), 2),
            'average_physical_hours': round(mean(s['physical_hours'] for s in self.students), 2)
        }