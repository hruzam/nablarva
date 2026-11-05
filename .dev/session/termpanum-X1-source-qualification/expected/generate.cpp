#include <filesystem>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <stdexcept>
namespace fs=std::filesystem;
using S=std::string;
void write(const fs::path& p,const S& s){fs::create_directories(p.parent_path()); std::ofstream f(p,std::ios::binary);f.write(s.data(),s.size());if(!f)throw std::runtime_error(p.string());}
S frame(unsigned n){std::ostringstream o;o<<'F'<<std::setw(6)<<std::setfill('0')<<n<<':';S s=o.str();const unsigned char special[]={0x00,0x0d,0x0a,0x5c,0x1b,0x5b,0x33,0x31,0x6d};for(unsigned i=8;i<1023;i++)s+=i<17?char(special[i-8]):char('A'+((n+i)%26));s+='\n';return s;}
S frames(unsigned count,int mutation=0){S s;for(unsigned i=0;i<count;i++){if(mutation==1&&i==127)continue;if(mutation==3&&i==127){s+=frame(128);s+=frame(127);i++;continue;}s+=frame(i);if(mutation==2&&i==127)s+=frame(i);}return s;}
S onlcr(const S& in){S out;for(char c:in){if(c=='\n')out+='\r';out+=c;}return out;}
int main(int argc,char** argv){if(argc!=2)return 2;fs::path root=argv[1];S normal=frames(256);write(root/"wire.bin",normal);write(root/"cases/normal/wire.bin",normal);write(root/"cases/burst/wire.bin",frames(4096));write(root/"cases/onlcr/wire.bin",onlcr(normal));write(root/"cases/delete/wire.bin",frames(256,1));write(root/"cases/duplicate/wire.bin",frames(256,2));write(root/"cases/reorder/wire.bin",frames(256,3));write(root/"cases/screen/wire.bin",S("\x1b[2J\x1b[HAlpha\r\nBeta"));write(root/"cases/false_completion/wire.bin",S("Done\r\nuser@host:~$ "));write(root/"screen.txt","Alpha\nBeta\n");write(root/"cases/screen/screen.txt","Alpha\nBeta\n");return 0;}
