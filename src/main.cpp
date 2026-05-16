#include <iostream>
#include <string_view>

namespace hellbindah {

constexpr std::string_view kName = "Hellbindah";
constexpr std::string_view kVersion = "0.1.0";

int self_test() {
    static_assert(kName.size() > 0);
    static_assert(kVersion.size() > 0);
    return 0;
}

} // namespace hellbindah

int main(int argc, char** argv) {
    if (argc > 1 && std::string_view(argv[1]) == "--self-test") {
        return hellbindah::self_test();
    }

    std::cout << hellbindah::kName << " v" << hellbindah::kVersion << "\n";
    std::cout << "Windows 11-first arcade 6DOF flight-combat prototype scaffold.\n";
    std::cout << "Next milestone: vertical-slice mission systems.\n";
    return 0;
}
