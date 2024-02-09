#include <iostream>

using namespace std;

bool Binary(int arr[], int low, int high, int num)
{
    int mid = (low + high) / 2;
    while (low < high)
    {
        if (arr[mid] == num)

        {
            cout << arr[mid];

            return true;
        }
        else if (arr[mid] < num)
        {
            cout << arr[mid] << "\n";
            return Binary(arr, mid + 1, high, num);
        }
        else
        {
            cout << arr[mid] << "\n";
            return Binary(arr, low, mid - 1, num);
        }
    }
}

int main()
{
    int arr1[] = {10, 30, 50, 60, 70};
    int size = sizeof(arr1) / sizeof(int);

    bool new1 = Binary(arr1, 0, size - 1, 60);
    if (new1 == true)
    {
        cout << "true";
    }
    else
        cout << "false";
    return 0;
}