#include <iostream>
#include <fstream>
#include <chrono>
#include <iomanip>

using namespace std;
constexpr int CONST_SIZE_ARR[8] = { 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000 };
constexpr int A = -1, B = 1;

double* paste_sort(double* data, size_t n)
{
	for (int i = 1; i < n; i++)
		for (int j = i; j > 0 && data[j - 1] > data[j]; j--) // пока j>0 и элемент j-1 > j, x-массив int
			swap(data[j - 1], data[j]);        // меняем местами элементы j и j-1

	return data;
}

int main(void)
{
	std::ofstream out; 
	double min[8], max[8], avg[8] = { 0 };
	for (size_t i = 0; i < 8; i++)
	{
		min[i] = 20;
		max[i] = -20;
	}
	
	out.open("output.txt");
	size_t counter = 0;
	// get times for all tests
	for (auto value : CONST_SIZE_ARR)
	{
		double* data = new double[value];
		for (size_t i = 0; i < 20; i++)
		{
			data[i] = A + (B - A) * rand() / (float)RAND_MAX;

			chrono::high_resolution_clock::time_point start = chrono::high_resolution_clock::now();
			double* sorted_data = paste_sort(data, value);
			chrono::high_resolution_clock::time_point end = chrono::high_resolution_clock::now();
			chrono::duration<double, milli> milli_diff = end - start;
			if (milli_diff.count() < min[counter])
			{
				min[counter] = milli_diff.count();
			}
			if (milli_diff.count() > max[counter])
			{
				max[counter] = milli_diff.count();
			}
			avg[counter] += milli_diff.count();
		}
		avg[counter] /= 20;
		counter += 1;
		
	}
	
	//output data into the file output.txt
	out << "N min max avg" << endl;
	for (size_t i = 0; i < 8; i++)
	{
		
		out << std::setprecision(3) << CONST_SIZE_ARR[i] << " " << min[i] << " " << max[i] << " " << avg[i] << endl;
	}
	out.close();
	system("python graphics.py");
	return 0;
}