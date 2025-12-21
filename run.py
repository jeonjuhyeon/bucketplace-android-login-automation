import traceback
from test_login import *


def main():

    tests = [
        Login.Login_001,
        Login.Login_002,
        Login.Login_003,
        Login.Login_004,
        Login.Login_005,
        Login.Login_007,
        Login.Login_008,
    ]

    passed = 0
    failed = 0

    for test in tests:
        try:
            result = test()
            if result:
                passed += 1
            else:
                failed += 1
        except Exception:
            failed += 1
            print("Unexpected error occurred")
            traceback.print_exc()

    print("\n=== Test Summary ===")
    print(f"Total   : {len(tests)}")
    print(f"Passed  : {passed}")
    print(f"Failed  : {failed}")

    print("**Appium Test finish**")


if __name__ == "__main__":
    main()