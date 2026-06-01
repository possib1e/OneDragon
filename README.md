# OneDragon

OneDragon 是一个面向授权安全测试、白帽研究和教学场景的自动化流程项目，用于串联子域名收集、端口识别、目录扫描和漏洞扫描等常见步骤。

> 仅限在已获得明确授权的目标上使用。请遵守所在地法律法规和目标系统授权边界。

## 功能概览

- 子域名扫描：集成 OneForAll，并使用 massdns 对结果进行验证和补充。
- 端口扫描：通过 masscan 和 nmap 生成端口识别结果。
- 目录扫描：使用 ffuf 对 HTTP 服务进行常规目录探测。
- 漏洞扫描：预留 xray 与 AWVS 爬虫联动流程。
- 结果聚合：统一输出到 `output/<targets-file>/` 目录，便于后续整理。

## 快速开始

1. 将目标主域名写入目标文件，例如 `targets.txt`：

   ```text
   example.com
   ```

2. 运行主流程：

   ```bash
   python3 start.py targets.txt
   ```

3. 查看输出目录：

   ```text
   output/targets.txt/
   ```

## 输出文件

- `final-domains-ips.txt`：子域名解析原始结果。
- `urls_sub.txt`：整理后的子域名 URL。
- `ips_all.txt`：整理后的 IP 列表。
- `urls_ip.txt`：端口扫描阶段识别出的 Web 服务。
- `ip_port_scan_results.txt`：端口扫描结果。
- `urls_all.txt`：聚合后的 URL 列表。
- `ffuf_all.csv` / `ffuf_redup.txt`：ffuf 扫描结果与去重结果。

## 维护计划

近期维护重点：

- Docker 化运行环境，减少工具链安装成本。
- 增加配置文件，替代硬编码路径和参数。
- 改进日志输出和异常处理。
- 生成统一的扫描结果报告。
- 拆分模块边界，便于单独运行和测试。

## 历史说明

### 2026.06.01

- 整理 README 结构，补充授权使用提醒、输出文件说明和维护计划。
- 加强入口参数检查，避免缺少目标文件或传入非根目录文件时直接进入扫描流程。
- 调整输出目录清理逻辑，减少 shell 字符串拼接带来的误删风险。

### 2021.01.30

OneForAll 使用 massdns 爆破功能时可能出现无结果的情况；单独使用 massdns 和相同字典可以获得结果。因此当前流程关闭 OneForAll 的爆破功能，并单独实现 massdns 爆破与泛解析的简单排除逻辑。

### 2021.01.04

初版使用说明：将目标主域名填入目标文件后，通过 `python3 start.py targets.txt` 串联子域名、端口、目录和漏洞扫描流程。

## License

This project is licensed under the MIT License.
