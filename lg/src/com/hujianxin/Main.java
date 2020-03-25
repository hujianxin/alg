package com.hujianxin;

import java.util.LinkedList;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    int N = scanner.nextInt(), L = scanner.nextInt();
    int A = scanner.nextInt(), B = scanner.nextInt();
    int maxValue = 0x3f3f3f3f;

    int[] m = new int[L + 1], dp = new int[L + 1];

    for (int i = 0; i < N; i++) {
      int s = scanner.nextInt(), e = scanner.nextInt();
      m[s + 1]++;
      m[e]--;
    }

    for (int i = 1; i <= L; i++) {
      m[i] += m[i - 1];
      dp[i] = maxValue;
    }

    LinkedList<Integer> q = new LinkedList<Integer>();
    for (int i = 2 * A; i <= L; i += 2) {
      while (!q.isEmpty() && dp[q.getFirst()] > dp[i - 2 * A]) {
        q.removeFirst();
      }
      q.addFirst(i - 2 * A);
      while (!q.isEmpty() && q.getLast() < i - 2 * B) {
        q.removeLast();
      }
      if (m[i] == 0) {
        dp[i] = dp[q.getLast()] + 1;
      }
    }

    if (dp[L] >= maxValue) {
      System.out.println(-1);
    } else {
      System.out.println(dp[L]);
    }
  }

}
