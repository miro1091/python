#include <stdio.h>
#include <time.h>

#define COL 9000

int main(void) {
	int c, d, k, sum = 0;

	double result[3][COL];
	double x[3][COL];
	double y[3][COL];

	for (d = 0; d < 3; d++) {
		for (c = 0; c < COL; c++) {
			x[d][c] = 0;
			y[d][c] = 0;
			result[d][c] = 0;
		}
	}


	for (c = 0; c < COL; c++) {
		x[0][c] = c;
		x[1][c] = COL - c;
		x[2][c] = 2 * COL - c;
		y[0][c] = x[2][c];
		y[1][c] = x[1][c];
		y[2][c] = x[0][c];
	}

	double x_rows = sizeof(x) / sizeof(x[0]);
	double x_columns = sizeof(x[0]) / sizeof(x[0][0]);

	clock_t begin = clock();

	for (c = 0; c < x_rows; c++)
	{
		for (d = 0; d < x_columns; d++)
		{
			for (k = 0; k < x_rows; k++)
			{
				sum += x[c][k] * y[k][d];
			}
			result[c][d] = sum;
			sum = 0;
		}
	}

	clock_t end = clock();

	/*for (c = 0; c < 3; c++)
	{
		for (d = 0; d < COL; d++)
			printf("%.2f\t", result[c][d]);

		printf("\n");
	}*/

	double time_spent = ((double)(end - begin))/(CLOCKS_PER_SEC);
	printf("Execution time(s): %f\n", end);
	printf("Execution time(s): %f\n", time_spent);

	return 0;
}

// gcc -o matrix matrix.c
// ./matrix