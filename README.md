# drone-plugin-latest-delegate

get the latest delegate image for your harness account

optinally, set the latest custom delegate image for your account

## configuration

- `HARNESS_PLATFORM_API_KEY`: api key to authenticate to harness api (required)
- `HARNESS_ENDPOINT`: harness url for your account (default: `app.harness.io`)

### to set the latest custom image for your account

- `DELEGATE_TAG`: delegate tag to use for the latest in your account, format: `<repo>/<image>:<tag>` (default: ` `)
- `VALID_TILL_NEXT_RELEASE`: if set to true, harness will override your custom tag when new delegate is released (default: `false`)
- `VALID_FOR_DAYS`: days after which harness will override your custom tag (default: `180`)

## usage

get latest

```yaml
- step:
    type: Plugin
    name: latest delegate
    identifier: latest_delegate
    spec:
      connectorRef: account.dockerhub
      image: rssnyder/drone-plugin-latest-delegate
      settings:
        HARNESS_PLATFORM_API_KEY: <+secrets.getValue("account.api")>
```

set latest

```yaml
- step:
    type: Plugin
    name: set latest delegate
    identifier: set_latest_delegate
    spec:
      connectorRef: account.dockerhub
      image: rssnyder/drone-plugin-latest-delegate
      settings:
        HARNESS_PLATFORM_API_KEY: <+secrets.getValue("account.api")>
        DELEGATE_TAG: companyrepo/harness_delegate:latest
```

## output

when getting latest

- `latestSupportedVersion`
- `latestSupportedMinimalVersion`

when setting latest

none

