#include <iostream>

using namespace std;

bool TernarySearch(int arr[], int low, int high, int num)
{
    int mid1 = low + (high - low) / 3;
    int mid2 = high - (high - low) / 3;

    while (low <= high)

    {
        if (arr[mid1] == num || arr[mid2] == num)
        {
            return true;
        }
        else if (arr[mid1] > num && arr[mid2] < num)
        {
            return TernarySearch(arr, mid1 + 1, mid2 + 1, num);
        }
        else if (arr[mid1] > num)
        {
            return TernarySearch(arr, low, mid1 - 1, num);
        }
        else if (arr[mid2] < num)
        {
            return TernarySearch(arr, mid2 + 1, high, num);
        }
        else
            return false;
    }
    return false;
}

int main()
{
    int arr1[] = {10, 30, 50, 60, 70};
    int size = sizeof(arr1) / sizeof(int);
    bool new1 = TernarySearch(arr1, 0, size - 1, 20);
    if (new1 == true)
    {
        cout << "Achee";
    }
    else
        cout << "Naai";
    return 0;
}