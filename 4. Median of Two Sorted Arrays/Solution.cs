public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        int[] nums = nums1.Concat(nums2).ToArray();
        Array.Sort(nums);
        if (nums.Length % 2 == 1)
            return nums[nums.Length / 2];
        else
            return (nums[nums.Length / 2 - 1] + nums[nums.Length / 2]) / 2.0;
    }
}