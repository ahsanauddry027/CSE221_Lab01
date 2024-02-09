#include <iostream>

using namespace std;

void mergeSort(int arr[], int start, int mid, int end)
{
    int size1 = mid - start + 1;
    int size2 = end - mid;

    int temp1[size1];
    int temp2[size2];

    for (int i = 0; i < size1; i++)
    {
        temp1[i] = arr[start + i];
    }
    for (int i = 0; i < size2; i++)
    {
        temp2[i] = arr[mid + 1 + i];
    }
    int i = 0;
    int j = 0;
    int k = start;

    while (i < size1 && j < size2)
    {
        if (temp1[i] < temp2[j])
        {
            arr[k] = temp1[i];
            i++;
            k++;
        }
        else
        {
            arr[k] = temp2[j];
            j++;
            k++;
        }
    }
    while (i < size1)
    {
        arr[k] = temp1[i];
        i++;
        k++;
    }
    while (j < size2)
    {
        arr[k] = temp1[j];
        j++;
        k++;
    }
}

void mergeDivide(int arr[], int start, int end)
{
    if (start < end)
    {
        int mid = (start + end) / 2;
        mergeDivide(arr, start, mid);
        mergeDivide(arr, mid + 1, end);

        mergeSort(arr, start, mid, end);
    }
}
int main()
{
    int numbers[] = {8, 2, 5, 4};
    mergeDivide(numbers, 0, 3);
    // for (int i = 0; i < 4; i++)
    // {
    //     cout << numbers[i] << " ";
    // }
    // int r = 1;
    // int sum = r / 2;
    // cout << sum;
    return 0;
}