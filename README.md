# yum_cron

Ansible role to install and configure yum_cron,
yum-cron is auto-update mechanism

## Installation

```yaml
   ansible-galaxy install zerodowntime.yum_cron
```

## Requirements

This role requires Ansible 2.5 or higher.

Supported platforms:

```yaml
  platforms:
    - name: EL
      versions:
        - 7
```

## Default role variables

| Variable name                 | Required? |  Type  | Description                                                         |
|:----------------------------- |:---------:|:------:| ------------------------------------------------------------------- |
| yum_cron__package_name        |    yes    | string | name of installed package                                           |
| yum_cron__package_state       |    yes    | string | installed package state                                             |
| yum_cron__daily_update_cmd    |    yes    | string | What kind of daily update to use                                    |
| yum_cron__hourly_update_cmd   |    yes    | string | What kind of hourly update to use                                   |
| yum_cron__email_to            |    no     | string | List of addresses to send messages to                               |
| yum_cron__exclude             |    no     |  list  | list of names excluded packages                                     |
| yum_cron__daily_random_sleep  |    yes    |  int   | Maximum amout of time to randomly sleep, in minutes for daily jobs. |
| yum_cron__hourly_random_sleep |    yes    |  int   | Maximum amout of time to randomly sleep, in minutes for hourly jobs |
| yum_cron__update_messages     |    yes    |  bool  | Whether a message should be emitted when updates are available      |
| yum_cron__download_updates    |    yes    |  bool  | Whether updates should be downloaded when they are available        |
| yum_cron__apply_updates       |    yes    |  bool  | Whether updates should be applied when they are available           |
| yum_cron__emit_via            |    yes    | string | How to send messages                                                |

**All variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

| Variable name          |  Type  | Description                    |
|:---------------------- |:------:|:------------------------------ |
| yum_cron__service_name | string | Service name                   |
| yum_cron__opt          |  dict  | config map for internal useage |

**All static variables are described in [vars/main.yml](vars/main.yml) file.**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:

        - role: zerodowntime.yum_cron
          yum_cron__exclude:
            - 'kernel*'
            - 'grub2*'
```

## License

[Apache License 2.0](LICENSE)

## Support

ansible@zerodowntime.pl
