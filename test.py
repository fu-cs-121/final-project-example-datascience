# test.py
from core import StudentAnalyzer
import csv
import os

def create_test_data():
    """Create a test CSV file"""
    filename = 'test_data.csv'
    data = [
        ['Student ID', 'Study Hours', 'Sleep Hours', 'Physical Activity Hours', 'Stress Level', 'CGPA'],
        [1, 6, 7, 2, 3, 3.8],
        [2, 4, 6, 1, 4, 3.2],
        [3, 2, 8, 0, 5, 2.4],
        [4, 8, 5, 3, 2, 3.9]
    ]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    return filename

def cleanup_test_data(filename):
    """Remove test CSV file"""
    if os.path.exists(filename):
        os.remove(filename)

def test_load_data():
    """Test data loading"""
    filename = create_test_data()
    analyzer = StudentAnalyzer(filename)
    
    assert len(analyzer.students) == 4, "Should load 4 students"
    assert isinstance(analyzer.students[0]['cgpa'], float), "CGPA should be float"
    assert isinstance(analyzer.students[0]['student_id'], int), "Student ID should be int"
    print("✓ Data loading test passed")
    
    cleanup_test_data(filename)

def test_average_cgpa():
    """Test CGPA calculation"""
    filename = create_test_data()
    analyzer = StudentAnalyzer(filename)
    
    avg_cgpa = analyzer.get_average_cgpa()
    assert isinstance(avg_cgpa, float), "Average should be float"
    assert 2.0 <= avg_cgpa <= 4.0, "CGPA should be between 2.0 and 4.0"
    print("✓ Average CGPA test passed")
    
    cleanup_test_data(filename)

def test_study_impact():
    """Test study hours analysis"""
    filename = create_test_data()
    analyzer = StudentAnalyzer(filename)
    
    impact = analyzer.get_study_impact()
    assert isinstance(impact, dict), "Should return dictionary"
    assert all(isinstance(v, float) for v in impact.values()), "All values should be floats"
    print("✓ Study impact test passed")
    
    cleanup_test_data(filename)

def test_stress_impact():
    """Test stress level analysis"""
    filename = create_test_data()
    analyzer = StudentAnalyzer(filename)
    
    impact = analyzer.get_stress_impact()
    assert isinstance(impact, dict), "Should return dictionary"
    assert all(isinstance(k, int) for k in impact.keys()), "Keys should be integers"
    print("✓ Stress impact test passed")
    
    cleanup_test_data(filename)

def test_top_performers():
    """Test top performers analysis"""
    filename = create_test_data()
    analyzer = StudentAnalyzer(filename)
    
    top = analyzer.find_top_performers(2)
    assert isinstance(top, dict), "Should return dictionary"
    assert 'study_hours' in top, "Should include study hours"
    assert 'average_cgpa' in top, "Should include average CGPA"
    print("✓ Top performers test passed")
    
    cleanup_test_data(filename)

def test_basic_stats():
    """Test basic statistics"""
    filename = create_test_data()
    analyzer = StudentAnalyzer(filename)
    
    stats = analyzer.get_basic_stats()
    assert isinstance(stats, dict), "Should return dictionary"
    assert stats['total_students'] == 4, "Should have correct student count"
    assert all(isinstance(v, (int, float)) for v in stats.values()), "Values should be numeric"
    print("✓ Basic stats test passed")
    
    cleanup_test_data(filename)

if __name__ == "__main__":
    print("Running Student Analyzer tests...\n")
    
    try:
        test_load_data()
        test_average_cgpa()
        test_study_impact()
        test_stress_impact()
        test_top_performers()
        test_basic_stats()
        
        print("\nAll tests passed successfully! ✨")
    except AssertionError as e:
        print(f"\n❌ Test failed: {str(e)}")