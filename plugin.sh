#!/bin/sh

# HARNESS_ACCOUNT_ID should be set by harness system

HARNESS_ENDPOINT="${PLUGIN_HARNESS_ENDPOINT:-app.harness.io}"

RESULT=$(curl "https://$HARNESS_ENDPOINT/ng/api/delegate-setup/latest-supported-version?accountIdentifier=$HARNESS_ACCOUNT_ID" -H "x-api-key: $PLUGIN_HARNESS_PLATFORM_API_KEY")

echo $RESULT | jq .

echo "latestSupportedVersion=$(echo $RESULT | jq '.resource.latestSupportedVersion')" >> $DRONE_OUTPUT
echo "latestSupportedMinimalVersion=$(echo $RESULT | jq '.resource.latestSupportedMinimalVersion')" >> $DRONE_OUTPUT
