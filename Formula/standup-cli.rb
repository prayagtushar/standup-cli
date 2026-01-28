class StandupCli < Formula
  include Language::Python::Virtualenv

  desc "Daily Standup Auto-Generator from git commits"
  homepage "https://github.com/prayagtushar/standup-cli"
  url "https://files.pythonhosted.org/packages/source/s/standup-cli/standup-cli-0.1.0.tar.gz"
  sha256 "/standup-cli-0.1.0-py3-none-any.whl.metadata"
  license "MIT"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    system bin/"standup-cli", "--help"
  end
end
