export default function handler(req, res) {
  res.status(200).json({
    platform: "Windows",
    version: "version-1e91b4133e334c9c",
    updatedAt: new Date().toISOString()
  });
}
