#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void fill(int m, int n, double *(array[n]))
{
    for (int i = 0; i < m; i++)
        for (int j = 0; j < n; j++)
            array[i][j] = (5 * i * i - 8) / (i * i * i + 1) + (sqrt(j + 1) - sqrt(j) - 0.5);
}

double find_max(int m, int n, double *(array[n]))
{
  double res = -1e9;
  for (int i = 0; i < m; i++)
      for (int j = 0; j < n; j++)
          if (fabs(array[i][j]) > res)
              res = fabs(array[i][j]);
  return res;
}

int main()
{
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
  printf("%lf", res * sqrt(n * m));
  return 0;
}
