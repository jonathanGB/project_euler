import java.util.*;

class prob_10 {
	public static void main(String args[]) {
		long start = System.currentTimeMillis();
		int numOfPrimes = 1;
		int sumOfPrimes = 2;
		LinkedList<Integer> primes = new LinkedList<Integer>();

		primes.add(2);

		for (int i = 3; i < 2000000; i += 2) {
			ListIterator<Integer> primesIterator = primes.listIterator();

			while (primesIterator.hasNext()) {
				if (i % primesIterator.next() == 0)
					break;
				else if (!primesIterator.hasNext()) {
					sumOfPrimes += i;
					numOfPrimes++;
					primesIterator.add(i);
				}
			}
		}

		long stop = System.currentTimeMillis();

		System.out.println("Number of primes: "+numOfPrimes+" / Sum of primes: "+sumOfPrimes+" / Time processed: "+((stop-start)/1000));
	}
}