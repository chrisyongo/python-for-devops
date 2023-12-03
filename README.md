# python-for-devops
AWS Cloud Cost Omptimization - Identifying stale resources
Identifying stale EBS snapshots 
In this example, I create a lambda function that identifies EBS snapshots that are no longer associated with any active EC2 instance and deletes them to save on storage costs

Description
The Lambda function fetches at EBS snapshots owned by the same account and als retrieves a list of active EC2 instances (running and stopped). For each snapshot, it checks for the associated volume (if it exists) is not associated with any instance. If it finds a stale snapshot, it deletes it, Effectively optimizing storage costs.