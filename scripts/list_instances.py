import boto3

def list_ec2_instances():
    """
    Lists EC2 instances using boto3 and displays their Name, ID, State, and Security Groups.
    """
    print("[*] Connecting to AWS EC2 in region ap-south-1...")
    
    # 1. Initialize the EC2 client (boto3 automatically loads credentials from ~/.aws/credentials)
    ec2 = boto3.client('ec2')
    
    # 2. Call describe_instances API
    response = ec2.describe_instances()
    
    print("\n" + "=" * 60)
    print(f"{'INSTANCE NAME':<18} | {'INSTANCE ID':<20} | {'STATE':<10}")
    print("=" * 60)
    
    found_any = False
    for reservation in response.get('Reservations', []):
        for instance in reservation.get('Instances', []):
            found_any = True
            instance_id = instance.get('InstanceId')
            state = instance.get('State', {}).get('Name')
            
            # Extract the 'Name' tag if it exists
            name = "Unnamed"
            for tag in instance.get('Tags', []):
                if tag.get('Key') == 'Name':
                    name = tag.get('Value')
                    break
                    
            print(f"{name:<18} | {instance_id:<20} | {state:<10}")
            
            # Print attached Security Groups (relevant for our containment phase!)
            sgs = [sg['GroupId'] + f" ({sg['GroupName']})" for sg in instance.get('SecurityGroups', [])]
            print(f"   -> Security Groups: {', '.join(sgs)}")
            print("-" * 60)
            
    if not found_any:
        print("No EC2 instances found in this region.")

if __name__ == '__main__':
    list_ec2_instances()
