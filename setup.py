import os
import subprocess
import json
import urllib.request

PAPERMC_API_BASEURL = "https://papermc.io/api/v2/projects/paper"
MC_VERSION = os.environ.get("MINECRAFT_VERSION")


def main():
    os.chdir("papermc")

    paper_build = get_latest_build_for_version(MC_VERSION)
    jar_name = f"paper-{MC_VERSION}-{paper_build}.jar"

    delete_older_jars(jar_name)
    
    if not os.path.exists(jar_name):
        download_server_jar(paper_build, jar_name)

    generate_eula_if_needed(jar_name)
    accept_eula()
    start_server(jar_name)


def download_server_jar(paper_build, jar_name):
    papermc_download_url = f"{PAPERMC_API_BASEURL}/versions/{MC_VERSION}/builds/{paper_build}/downloads/{jar_name}"
    urllib.request.urlretrieve(papermc_download_url, jar_name)


def delete_older_jars(current_jar_name):
    for file in os.listdir("."):
        if file.endswith(".jar") and file != current_jar_name:
            os.remove(file)


def get_latest_build_for_version(mc_version):
    with urllib.request.urlopen(
        f"{PAPERMC_API_BASEURL}/versions/{mc_version}"
    ) as response:
        data = json.loads(response.read().decode())
        return data["builds"][-1]


def generate_eula_if_needed(jar_name):
    if not os.path.exists("eula.txt"):
        subprocess.run(["java", "-jar", jar_name])


def accept_eula():
    subprocess.run(["sed", "-i", "s/eula=false/eula=true/g", "eula.txt"])


def start_server(jar_name):
    command = ["java", "-server", "-jar", jar_name, "nogui"]
    print(f"Running: {' '.join(command)}")
    subprocess.run(command)


if __name__ == "__main__":
    main()
