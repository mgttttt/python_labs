#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

void fill(int m, int n, double *(array[n]))
{
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
          {
            int k = i + 1;
            int l = j + 1;
            array[i][j] = sin(pow(1.3, k) - 1.2) + sin(l) - 1.0 / (1 + l * l);
          }
}

double find_max(int m, int n, double *(array[n]))
{
  double res = 0;
  for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
            res += array[i][j] * array[i][j];
  return res;
}

int main()
{
  clock_t begin = clock();
  int n, m;
  printf("Enter count of rows: ");
  scanf("%d", &m);
  printf("Enter count of columns: ");
  scanf("%d", &n);
  double **array = (double **)malloc(sizeof(double *) * m);
  if (!array)
  {
    printf("Memory allocation error!\n");
    exit(EXIT_FAILURE);
  }
  for (int i = 0; i < m; i++)
    array[i] = (double *)malloc(n * sizeof(double));
  fill(m, n, array);
  double res = find_max(m, n, array);
  printf("%lf\n", sqrt(res));
  clock_t end = clock();
  double time_spent = (double)(end - begin) / CLOCKS_PER_SEC * 100;
  printf("%lf мс\n", time_spent);
  return 0;
}
