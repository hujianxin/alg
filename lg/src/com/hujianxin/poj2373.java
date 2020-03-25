package com.hujianxin;

import java.util.LinkedList;
import java.util.Scanner;

public class poj2373 {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    // N: 有N头牛
    // L：山脊长度为L
    int N = scanner.nextInt(), L = scanner.nextInt();
    // A: 水龙头最小的喷洒半径
    // B：水龙头最大的喷洒半径
    int A = scanner.nextInt(), B = scanner.nextInt();

    // 一个经验值，这个地方不能用最大整型，后面会发生溢出
    int maxValue = 0x3f3f3f3f;

    // m 表示整个山脊的牛分布情况数组，m[i]==0表示，i这个地方，不会有牛出没
    // dp[i] 表示[0, i]这段山脊，最少放水龙头的个数
    // 由题意可知：
    // 1. i 不可能是基数
    // 2. i 必须大于等于2 * A
    // 3. i 不能出现在有牛出没的地方
    // 认识到上面这三个条件之后，dp[i] = min(dp[i - 2 * B] ... dp[i - 2 * A]) + 1
    // 求min(dp[i - 2 * B] ... dp[i - 2 * A])是一个O(B)的算法，而遍历整个山脊线需要L次
    // 所以整体是一个O(LB)的算法，这个算法超超时
    // 需要找一个O(1)的算法来求min(dp[i - 2 * B] ... dp[i - 2 * A]),这里使用了单调队列
    // 用单调递增的单调队列来维护dp数组中i - 2 * B ~ i - 2 * A的最小值
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
