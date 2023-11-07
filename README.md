# Group Project B

**Deployed at https://paste.unh.app** (Not Currently Running)

## Resources

### Phase 5

Final Report: https://docs.google.com/document/d/1enzWaSrkpXPCDcBytMpseu9JYs9eWM-UEKEa7QPvTYk/edit#

Presentation: https://docs.google.com/presentation/d/176cyM02XAdqNUm_bdo3sAwtto5S8TrV1XOQ4Lmq1QGs/edit?usp=sharing

### Gitlab

Gitlab Issues: https://gitlab.cs.unh.edu/groups/cs518/fall-2022/section-1/group-b/-/issues 

Gitlab Milestones: https://gitlab.cs.unh.edu/groups/cs518/fall-2022/section-1/group-b/-/milestones

### Previous Documents
Project Report 1: https://docs.google.com/document/d/1a6PDJ4PfhxSkNHoerTbaiObrz_5eGhA94qKN7n4TAME/edit?usp=sharing

Project Report 2: https://docs.google.com/document/d/1U9f356F-Zsj2oXWLq74vFXN7ka8dlNDsFzXyW9u0D70/edit?usp=sharing

Old Meeting Journal: https://docs.google.com/document/d/1zKhpssbQXz3uvpqdYMq-zZkDD_QiVJFS4Z5Zf0xixn4/

## Repository Structure

* **/DataService/** - Includes the Azure functions API and Python database reader (`data_service.py`)

* **/WebServer/** - Includes the Flask webserver, frontend templates, and static files

* **/Documentation/** - contains the final version of our arch diagrams, interaction diagrams, and written documentation for the `data_service.py` database reader and Azure functions

* **/Documentation/Planning/** - contains initial planning documents: old intros, user stories, personas, diagrams, and roadmap drafts from sprint 1

## Command Reference

Run mongoDB with powershell (replace `<username>` with username):

```cmd
& 'C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe' --dbpath='C:\Users\<username>\AppData\Local\mongodb\data'
```

Run azure cloud functions:

```cmd
cd ./DataService/
func start --python
```
Run flask in debug mode:

```cmd
cd ./WebServer
python app.py
```

Publish azure functions:
```cmd
cd ./DataService
func azure functionapp publish group-b-paste-site
```

Build and push docker image:
```cmd
docker login
cd ./WebServer
docker build --tag nfb1017/pastesite .
docker push nfb1017/pastesite
```
