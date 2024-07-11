#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void chuyenSoNguyenLon(int arr[100], int W, int a, int t){
  int i;
  long long z;
  for (i=t-1;i>=0;i--){
        z = pow(2,W*i);
        arr[i] = a/z;
        a = a%z;

  }
}

void chuyenVeSoNguyenLon( int arr[100],int m, int t ,int W)
{
    long long a = 0,z;
    int i;
   for(i = t-1 ; i>=0; i--)
    {
        z = pow(2,W *(i));
        a += arr[i]*z;
    }
    printf("\nSo do La: %lld", a);
}


void inMang(int Mang[100], int n){
  int i;
  printf("[ ");
  for (i=n-1; i>= 0; i--){
    printf("%d ", Mang[i]);
  }
  printf(" ] \n");
}

int cong(int a[100],int b[100],int c[100],int t,int W)
{
    int e = 0, i, w, h;
    for( i = 0; i < t; i++)
    {
        w = a[i] + b[i] + e;
        h = pow(2, W);
        c[i]= w % h;
        if(w >= h)
        {
          e = 1;
        }
        else
        {
          e = 0;
        }
    }
    return e;
}


int tru(int a[100],int b[100],int c[100],int t, int W)
{
    int e = 0, i, w, h;
    for(i = 0; i < t; i++)
    {
        w =  a[i] - b[i] - e;
        h = pow(2, W);
        if(w < 0)
        {
            c[i]= h+w;
            e = 1;
        }
        else if(w >= h)
        {
            e = 1;
            c[i] = w%h;
        }
        else
        {
            e = 0;
            c[i] = w%h;
        }
    }

    return e;
}

int main()
{
    int arr[100], brr[100], c[100], P[100],W=8, m, t, e, i;
    long long p = 2147483647,a,b;
    printf("Nhap a, b: ");
    scanf("%lld%lld", &a, &b);
    // tính logarit cơ số 2 của p double result = log(x) / log(2) bởi vì ban đầu là logarit cơ số e nên phải chia để chuyển ra logarit cơ số 2
    m = ceil(log(p)/log(2));
    t = ceil((double)m/W);
    chuyenSoNguyenLon(arr,W,a,t);
    chuyenSoNguyenLon(brr,W,b,t);
    chuyenSoNguyenLon(P,W,p,t);
    printf("--------------------------------\n");
    printf("Ma tran cua P:\n");
    inMang(arr,t);
    inMang(brr,t);
    e = cong(arr,brr,c,t,W);
    printf("Ket qua cong tren truong huu han:\n");
    inMang(c,t);
    chuyenVeSoNguyenLon(c,m,t,W);
    return 0;
}
