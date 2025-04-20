export default function handler(req, res) {
  const versions = {
    Windows: "version-1e91b4133e334c9c",
  };

  const { platform } = req.query;
  const version = versions[platform];

  if (version) {
    res.status(200).json({ platform, version });
  } else {
    res.status(404).json({ error: "Platform not found" });
  }
}
