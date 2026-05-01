import argparse
from mcp_manager import MCPManager

def main():
    manager = MCPManager()
    parser = argparse.ArgumentParser(
        description="🐾 MCP Auto-Pack & Publisher - リバにゃんの魔法のツール",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  mcp backup                      # 装備を保存して安全を確保するにゃ！
  mcp install starter-pack        # 基本の力を授けるにゃ
  mcp install earning-pack        # 収益化構成を即インストールだにゃ！
  mcp list                        # 装備を確認するにゃ
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Backup command
    subparsers.add_parser("backup", help="装備を保存して安全を確保するにゃ！")
    
    # Install command
    install_parser = subparsers.add_parser("install", help="完成済みパックを一括インストール")
    install_parser.add_argument("pack_name", help="Pack name (starter-pack or earning-pack)")
    
    # List command
    subparsers.add_parser("list", help="装備を確認するにゃ")
    
    args = parser.parse_args()
    
    if args.command == "backup":
        manager.backup_config()
    elif args.command == "install":
        manager.install_pack(args.pack_name)
    elif args.command == "list":
        manager.list_mcp_servers()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
