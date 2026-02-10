"""
Test Script for Mental Health Analytics Dashboard
Run this to verify your setup is correct before launching the dashboard
"""

import sys

def test_python_version():
    """Check Python version"""
    print("🐍 Testing Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Need 3.8+")
        return False

def test_imports():
    """Test if all required packages are installed"""
    print("\n📦 Testing package imports...")
    
    packages = {
        'streamlit': 'streamlit',
        'pandas': 'pandas',
        'numpy': 'numpy',
        'matplotlib': 'matplotlib.pyplot',
        'seaborn': 'seaborn',
        'plotly': 'plotly.express',
        'sklearn': 'sklearn.ensemble'
    }
    
    all_ok = True
    for name, import_path in packages.items():
        try:
            __import__(import_path)
            print(f"   ✅ {name} - OK")
        except ImportError:
            print(f"   ❌ {name} - NOT FOUND")
            all_ok = False
    
    return all_ok

def test_data_file():
    """Check if CSV file exists"""
    print("\n📄 Testing data file...")
    try:
        import pandas as pd
        df = pd.read_csv('synthetic_mental_health_dataset__1_.csv')
        print(f"   ✅ CSV file found - {len(df)} rows, {len(df.columns)} columns")
        return True
    except FileNotFoundError:
        print("   ❌ CSV file not found!")
        print("      Make sure 'synthetic_mental_health_dataset__1_.csv' is in this folder")
        return False
    except Exception as e:
        print(f"   ❌ Error reading CSV: {e}")
        return False

def test_app_file():
    """Check if app.py exists"""
    print("\n📱 Testing app file...")
    try:
        with open('app.py', 'r') as f:
            content = f.read()
            if 'streamlit' in content and 'def main()' in content:
                print("   ✅ app.py found and looks correct")
                return True
            else:
                print("   ⚠️  app.py found but might be incomplete")
                return False
    except FileNotFoundError:
        print("   ❌ app.py not found!")
        return False

def test_requirements():
    """Check if requirements.txt exists"""
    print("\n📋 Testing requirements file...")
    try:
        with open('requirements.txt', 'r') as f:
            reqs = f.read()
            print("   ✅ requirements.txt found")
            print(f"      Contains {len(reqs.splitlines())} packages")
            return True
    except FileNotFoundError:
        print("   ❌ requirements.txt not found!")
        return False

def main():
    """Run all tests"""
    print("=" * 60)
    print("🧪 Mental Health Dashboard - Setup Verification Test")
    print("=" * 60)
    
    results = []
    
    # Run tests
    results.append(("Python Version", test_python_version()))
    results.append(("Package Imports", test_imports()))
    results.append(("Data File", test_data_file()))
    results.append(("App File", test_app_file()))
    results.append(("Requirements File", test_requirements()))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name:.<40} {status}")
    
    print("=" * 60)
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! You're ready to run the dashboard!")
        print("\nRun this command to start:")
        print("   streamlit run app.py")
    else:
        print("\n⚠️  Some tests failed. Please fix the issues above.")
        print("\nCommon solutions:")
        print("   • Missing packages? Run: pip install -r requirements.txt")
        print("   • Missing files? Check that all files are in the same folder")
        print("   • Wrong Python version? Install Python 3.8 or higher")
    
    print("=" * 60)

if __name__ == "__main__":
    main()
