# Task 03 Evidence Checklist

Save actual screenshots/output in `docs/evidence/`. Do not invent or edit terminal results to make tests look successful.

- [ ] `docker --version`
- [ ] `docker compose version`
- [ ] `docker compose build` succeeds
- [ ] `docker compose ps` shows service status
- [ ] `/health` response is recorded
- [ ] App image size is measured in bytes and converted to MiB
- [ ] `docker inspect` confirms `10001:10001`
- [ ] App logs are captured
- [ ] Persistence/restart test is completed if required by the rubric
- [ ] Public repository is checked in a private/incognito browser
