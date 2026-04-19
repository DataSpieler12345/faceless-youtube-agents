import requests
from lib.config import ZERNIO_BASE_URL, ZERNIO_API_KEY


def _headers():
    return {
        "Authorization": f"Bearer {ZERNIO_API_KEY}",
        "Content-Type": "application/json",
    }


def list_profiles() -> list[dict]:
    resp = requests.get(f"{ZERNIO_BASE_URL}/profiles", headers=_headers(), timeout=30)
    resp.raise_for_status()
    return resp.json()


def get_youtube_account_id() -> str:
    """Find the first connected YouTube account ID."""
    profiles = list_profiles()
    for profile in profiles:
        accounts = profile.get("accounts", [])
        if isinstance(profiles, dict):
            accounts = profiles.get("accounts", profiles.get("data", []))
            break
        for account in accounts if isinstance(accounts, list) else []:
            if account.get("platform") == "youtube":
                return account.get("id", account.get("accountId", ""))

    if isinstance(profiles, list):
        for item in profiles:
            if isinstance(item, dict) and item.get("platform") == "youtube":
                return item.get("id", item.get("accountId", ""))

    raise RuntimeError(
        "No YouTube account found. Connect your YouTube channel at https://zernio.com first."
    )


def upload_video(
    video_url: str,
    title: str,
    description: str,
    tags: list[str] = None,
    thumbnail_url: str = "",
    visibility: str = "private",
    account_id: str = "",
) -> dict:
    """Upload a video to YouTube via Zernio API as draft (private)."""
    if not account_id:
        account_id = get_youtube_account_id()

    payload = {
        "content": description,
        "platforms": [
            {
                "platform": "youtube",
                "accountId": account_id,
                "platformSpecificData": {
                    "title": title,
                    "visibility": visibility,
                },
            }
        ],
        "mediaItems": [{"type": "video", "url": video_url}],
        "publishNow": True,
        "tags": tags or [],
    }

    if thumbnail_url:
        payload["mediaItems"].append({"type": "thumbnail", "url": thumbnail_url})

    resp = requests.post(
        f"{ZERNIO_BASE_URL}/posts",
        headers=_headers(),
        json=payload,
        timeout=120,
    )
    resp.raise_for_status()
    data = resp.json()
    print(f"  YouTube upload submitted: {data}")
    return data


def get_post_status(post_id: str) -> dict:
    resp = requests.get(
        f"{ZERNIO_BASE_URL}/posts/{post_id}",
        headers=_headers(),
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json()
