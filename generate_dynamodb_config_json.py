import boto3
import json

# Initialize the DynamoDB client
dynamodb_client = boto3.client('dynamodb', region_name='ap-south-1')  # Replace with your AWS region

# List of DynamoDB table names (extracted from your provided input)
table_names = [
    "MUS_Adda247-3DModelService_uploadedMedia", "MUS_Adda247-AISolver_uploadedMedia",
    "MUS_Adda247-AssessmentCreationService_uploadedMedia", "MUS_Adda247-AssessmentEvaluationService_uploadedMedia",
    "MUS_Adda247-GlobalConfigService_uploadedMedia", "MUS_Adda247-LCSService_uploadedMedia",
    "MUS_Adda247-LiveClassComments_uploadedMedia", "MUS_Adda247-LiveClass_uploadedMedia",
    "MUS_Adda247-Miscellaneous_uploadedMedia", "MUS_Adda247-OmrScanner_uploadedMedia",
    "MUS_Adda247-QuestionService-CMS_uploadedMedia", "MUS_Adda247-UserProfile_uploadedMedia",
    "MUS_Adda247-VideoSolutions_uploadedMedia", "MUS_Adda247-VideoStreamingMediaService_uploadedMedia",
    "MUS_Adda247-VideoStreamingService_uploadedMedia", "MUS_AddaSocial_uploadedMedia",
    "MUS_AddaVideo_uploadedMedia", "MUS_AdmitcardUploadService_uploadedMedia",
    "MUS_Sankalp-3DModelService_uploadedMedia", "MUS_Sankalp-GlobalConfigService_uploadedMedia",
    "MUS_Sankalp-LCSService_uploadedMedia", "MUS_Sankalp-LiveClassComments_uploadedMedia",
    "MUS_Sankalp-UserProfile_uploadedMedia", "MUS_Sankalp-VideoSolutions_uploadedMedia",
    "MUS_Sankalp-VideoStreamingMediaService_uploadedMedia", "MUS_Sankalp-VideoStreamingService_uploadedMedia",
    "MUS_SankalpSocial_uploadedMedia", "MUS_Skills-AssessmentEvaluationService_uploadedMedia",
    "MUS_Skills-LCSService_uploadedMedia", "MUS_Skills-LiveClassComments_uploadedMedia",
    "MUS_Skills-Miscellaneous_uploadedMedia", "MUS_Skills-QuestionService-CMS_uploadedMedia",
    "MUS_Skills-UserProfile_uploadedMedia", "MUS_Skills-VideoStreamingMediaService_uploadedMedia",
    "MUS_Skills-VideoStreamingService_uploadedMedia", "MUS_SkillsSocial_uploadedMedia",
    "MUS_StudyIQ-QuestionService-CMS_uploadedMedia", "MUS_StudyIq-AssessmentCreationService_uploadedMedia",
    "MUS_StudyIq-AssessmentEvaluationService_uploadedMedia", "MUS_StudyIq-LCSService_uploadedMedia",
    "MUS_StudyIq-LiveClassComments_uploadedMedia", "MUS_testService", "STIQAS_attachments", "STIQAS_review_options",
    "STIQAS_user_reviews", "STIQCS_attachments", "STIQCS_review_options", "STIQCS_user_reviews",
    "STIQMS_attachments", "STIQMS_review_options", "STIQMS_user_reviews", "STIQTS_attachments",
    "STIQTS_review_options", "STIQTS_user_reviews", "addaRS_delete_comment", "addaRS_discussion_attachments",
    "addaRS_discussions_likes", "addaRS_pin_comment", "addaRS_post_comment", "addaRS_post_subcomment", "addaRS_posts",
    "addaRS_report_reason", "addaRS_reported_comments", "addaRS_reported_subComments", "addaRS_stop_words",
    "addaWL_delete_comment", "addaWL_discussion_attachments", "addaWL_discussions_likes", "addaWL_pin_comment",
    "addaWL_post_comment", "addaWL_post_subcomment", "addaWL_posts", "addaWL_report_reason", "addaWL_reported_comments",
    "addaWL_reported_subComments", "addaWL_stop_words", "adda_user_profile_detailed_info", "addasocial_config",
    "addasocial_discussion_attachments", "addasocial_discussions_feedback", "addasocial_discussions_likes",
    "addasocial_faculty_lookup_table", "addasocial_group", "addasocial_group_admins", "addasocial_group_deletedAdmins",
    "addasocial_group_followers", "addasocial_group_followers_deleted", "addasocial_hidden_posts", "addasocial_latest_post",
    "addasocial_mcq_options", "addasocial_mcq_response", "addasocial_notification_log", "addasocial_notification_off_posts",
    "addasocial_notifications_watcher", "addasocial_pin_post", "addasocial_post_bookmarked", "addasocial_post_comment",
    "addasocial_post_count", "addasocial_post_subcomment", "addasocial_posts", "addasocial_report_reason",
    "addasocial_reported_posts", "blacklisted_users_table", "category_table", "category_topic_table",
    "migration_comment_legacy", "migration_post_legacy", "migration_subComment_legacy", "migration_topicId_NotFound",
    "rds_admin_details", "rds_users_details", "sankalpFS_delete_comment", "sankalpFS_discussion_attachments",
    "sankalpFS_discussions_likes", "sankalpFS_pin_comment", "sankalpFS_post_comment", "sankalpFS_post_subcomment",
    "sankalpFS_posts", "sankalpFS_report_reason", "sankalpFS_reported_comments", "sankalpFS_reported_subComments",
    "sankalpFS_stop_words", "sankalp_discussion_attachments", "sankalp_discussions_likes", "sankalp_faculty_lookup_table",
    "sankalp_group", "sankalp_group_admins", "sankalp_group_deletedAdmins", "sankalp_group_followers", "sankalp_group_followers_deleted",
    "sankalp_hidden_posts", "sankalp_latest_post", "sankalp_mcq_options", "sankalp_mcq_response", "sankalp_notification_log",
    "sankalp_notification_off_posts", "sankalp_notifications_watcher", "sankalp_pin_post", "sankalp_post_bookmarked",
    "sankalp_post_comment", "sankalp_post_count", "sankalp_post_subcomment", "sankalp_posts", "sankalp_reported_posts",
    "service_configuration", "service_moderation_policy", "skillRS_delete_comment", "skillRS_discussion_attachments",
    "skillRS_discussions_likes", "skillRS_pin_comment", "skillRS_post_comment", "skillRS_post_subcomment", "skillRS_posts",
    "skillRS_report_reason", "skillRS_reported_comments", "skillRS_reported_subComments", "skillRS_stop_words",
    "skillWL_delete_comment", "skillWL_discussions_likes", "skillWL_pin_comment", "skillWL_post_comment", "skillWL_post_subcomment",
    "skillWL_posts", "skillWL_report_reason", "skillWL_reported_comments", "skillWL_reported_subComments", "skillWL_stop_words",
    "skill_discussion_attachments", "skills_config", "skills_discussion_attachments", "skills_discussions_feedback",
    "skills_discussions_likes", "skills_faculty_lookup_table", "skills_grouop_deletedAdmins", "skills_group",
    "skills_group_admins", "skills_group_deletedAdmins", "skills_group_followers", "skills_group_followers_deleted",
    "skills_hidden_posts", "skills_latest_post", "skills_mcq_options", "skills_mcq_response", "skills_notification_log",
    "skills_notification_off_posts", "skills_notifications_watcher", "skills_pin_post", "skills_post_bookmarked",
    "skills_post_comment", "skills_post_count", "skills_post_subcomment", "skills_posts", "skills_reported_posts",
    "studyIQFS_delete_comment", "studyIQFS_delete_subComment", "studyIQFS_discussion_attachments", "studyIQFS_discussions_likes",
    "studyIQFS_pin_comment", "studyIQFS_post_comment", "studyIQFS_post_subcomment", "studyIQFS_posts", "studyIQFS_report_reason",
    "studyIQFS_reported_comments", "studyIQFS_reported_subComments", "studyIQFS_stop_words", "studyIQNCERT_attachments",
    "studyIQNCERT_review_options", "studyIQNCERT_user_reviews", "sub_category_table", "test_users_table", "uploaded_media"
]

# Function to extract necessary configuration for Terraform
def extract_table_config(table_description):
    table = table_description['Table']
    config = {
        "TableName": table['TableName'],
        "AttributeDefinitions": table['AttributeDefinitions'],
        "KeySchema": table['KeySchema'],
        "ProvisionedThroughput": {
            "ReadCapacityUnits": table.get('ProvisionedThroughput', {}).get('ReadCapacityUnits', 5),
            "WriteCapacityUnits": table.get('ProvisionedThroughput', {}).get('WriteCapacityUnits', 5)
        },
        "BillingMode": table.get('BillingModeSummary', {}).get('BillingMode', 'PAY_PER_REQUEST'),
        "StreamSpecification": {
            "StreamEnabled": table.get('StreamSpecification', {}).get('StreamEnabled', False)
        },
        "GlobalSecondaryIndexes": [],
        "LocalSecondaryIndexes": []
    }

    # Include GSI configurations if any
    if 'GlobalSecondaryIndexes' in table:
        for gsi in table['GlobalSecondaryIndexes']:
            config['GlobalSecondaryIndexes'].append({
                "IndexName": gsi['IndexName'],
                "KeySchema": gsi['KeySchema'],
                "Projection": gsi['Projection'],
                "ProvisionedThroughput": {
                    "ReadCapacityUnits": gsi['ProvisionedThroughput']['ReadCapacityUnits'],
                    "WriteCapacityUnits": gsi['ProvisionedThroughput']['WriteCapacityUnits']
                }
            })
    
    # Include LSI configurations if any
    if 'LocalSecondaryIndexes' in table:
        for lsi in table['LocalSecondaryIndexes']:
            config['LocalSecondaryIndexes'].append({
                "IndexName": lsi['IndexName'],
                "KeySchema": lsi['KeySchema'],
                "Projection": lsi['Projection']
            })
    
    return config

# Collect configurations for all tables
configs = []

for table_name in table_names:
    try:
        response = dynamodb_client.describe_table(TableName=table_name)
        table_config = extract_table_config(response)
        configs.append(table_config)
        print(f"Fetched configuration for table: {table_name}")
    except dynamodb_client.exceptions.ResourceNotFoundException:
        print(f"Table {table_name} not found. Skipping.")
    except Exception as e:
        print(f"Error fetching table {table_name}: {e}")

# Write configurations to a JSON file
with open('dynamodb_config.json', 'w') as file:
    json.dump(configs, file, indent=2, default=str)

print("DynamoDB configurations have been written to dynamodb_config.json")