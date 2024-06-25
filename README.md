# drone-plugin-latest delegate

get the latest delegate image for your harness account

## configuration

- `HARNESS_PLATFORM_API_KEY`: api key to authenticate to harness api (required)
- `HARNESS_ENDPOINT`: harness url for your account (default: `app.harness.io`)

### to set the latest custom image for your account

- `DELEGATE_TAG`: delegate tag to use for the latest in your account, format: `<repo>/<image>:<tag>` (default: ``)
- `VALID_TILL_NEXT_RELEASE`: if set to true, harness will override your custom tag when new delegate is released (default: `false`)
- `VALID_FOR_DAYS`: days after which harness will override your custom tag (default: `180`)

## output

- `latestSupportedVersion`
- `latestSupportedMinimalVersion`
