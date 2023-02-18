#include <iostream>
#include <fstream>
#include <chrono>
#include <iomanip>
#include <string>
using namespace std;


double* data;
constexpr int CONST_SIZE_ARR[8] = { 1000, 2000, 4000, 8000, 16000, 32000, 64000, 128000 };
constexpr int A = -1, B = 1;

void generation(size_t count_of_elems, size_t flag)
{
	switch (flag)
	{
		case 1:
		{
			for (int i = 0; i < count_of_elems; ++i)
			{
				::data[i] = count_of_elems - i; // отсортированный изначально
			}
			break;
		}
		case 2:
		{
			for (int i = 0; i < count_of_elems; ++i)
			{
				::data[i] = 1; // одинаковые элементы
			}
			break;
		}
		case 3:
		{
			for (int i = 0; i < count_of_elems; ++i)
			{
				::data[i] = A + (B - A) * rand() / (float)RAND_MAX; 
			}
			for (int i = 0; i < count_of_elems - 1; ++i)
				swap(::data[i], ::data[i / 2]);   // с максимальным количеством сравнений при выборе среднего элемента в качестве опорного
			break;
		}
		case 4:
		{
			for (int i = 0; i < count_of_elems; ++i)
			{
				::data[i] = A + (B - A) * rand() / (float)RAND_MAX;  // рандом
			}
		}
	}
}


int quick_sort(int S, int P)
{
	int k1 = S, k2 = P;
	int recursion_count = 0;
	double mid = ::data[(k1 + k2) / 2];
	while (k1 <= k2)
	{
		while (::data[k1] < mid)
			++k1;
		while (::data[k2] > mid)
			--k2;
		if (k1 <= k2)
		{
			swap(::data[k1], ::data[k2]);
			++k1;
			--k2;
		}
	}
	if (S < k2)
	{
		recursion_count += quick_sort(S, k2);
		recursion_count += 1;
	}
	if (P > k1)
	{
		recursion_count += quick_sort(k1, P);
		recursion_count += 1;
	}

	return recursion_count;
}


void tests(size_t flag, string filename) 
{
	std::ofstream out;
	int min[8], max[8] = { 0 }, avg[8] = { 0 };

	for (size_t i = 0; i < 8; i++)
		min[i] = 999999;


	out.open(filename);
	size_t counter = 0;

	for (auto value : CONST_SIZE_ARR)
	{
		for (size_t i = 0; i < 20; i++)
		{
			size_t recur_count = 0;
			::data = new double[value];
			generation(value, flag);
			
		
			recur_count = quick_sort(0, value);
			if (recur_count < min[counter])
			{
				min[counter] = recur_count;
			}
			if (recur_count > max[counter])
			{
				max[counter] = recur_count;
			}
			avg[counter] += recur_count;
		}
		avg[counter] /= 20;
		counter += 1;
	}

	//output data into the file 
	out << "N min max avg" << endl;
	for (size_t i = 0; i < 8; i++)
	{

		out << std::setprecision(3) << CONST_SIZE_ARR[i] << " " << min[i] << " " << max[i] << " " << avg[i] << endl;
	}
	out.close();
}


int main(void)
{
	srand(time(0));

	tests(1, "output_1.txt"); // отсортированный изначально
	tests(2, "output_2.txt"); // одинаковые элементы
	tests(3, "output_3.txt"); // с максимальным количеством сравнений при выборе среднего элемента в качестве опорного
	tests(4, "output_4.txt"); // рандом
	/*system("python graphics.py");*/
	return 0;
}
	
