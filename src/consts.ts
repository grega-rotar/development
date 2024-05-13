import type { Site, Page, Links, Socials } from "@types"

// Global
export const SITE: Site = {
  TITLE: "Grega Rotar",
  DESCRIPTION: "Welcome to Grega Rotar's portfilio",
  AUTHOR: "Grega Rotar",
}

// Work Page
export const WORK: Page = {
  TITLE: "Work",
  DESCRIPTION: "Places I have worked.",
}

// Blog Page
export const BLOG: Page = {
  TITLE: "Blog",
  DESCRIPTION: "Writing on topics I am passionate about.",
}

// Projects Page 
export const PROJECTS: Page = {
  TITLE: "Projects",
  DESCRIPTION: "Recent projects I have worked on.",
}

// HomeLab Page 
export const HOMELAB: Page = {
  TITLE: "Home Lab",
  DESCRIPTION: "My home lab insight.",
}

// Search Page
export const SEARCH: Page = {
  TITLE: "Search",
  DESCRIPTION: "Search all posts and projects by keyword.",
}

// Links
export const LINKS: Links = [
  { 
    TEXT: "Home", 
    HREF: "/", 
  },
  { 
    TEXT: "Work", 
    HREF: "/work", 
  },
  { 
    TEXT: "Blog", 
    HREF: "/blog", 
  },
  { 
    TEXT: "Projects", 
    HREF: "/projects", 
  },
  {
    TEXT: "Home Lab",
    HREF: "/homeLab"
  },
]

// Socials
export const SOCIALS: Socials = [
  { 
    NAME: "Email",
    ICON: "email", 
    TEXT: "grega@etiam.si",
    HREF: "mailto:grega@etiam.si",
  },
  { 
    NAME: "Github",
    ICON: "github",
    TEXT: "grega-rotar",
    HREF: "https://github.com/grega-rotar"
  },
  { 
    NAME: "Instagram",
    ICON: "instagram",
    TEXT: "grotar123",
    HREF: "https://instagram.com/grotar123"
  },
  // { 
  //   NAME: "LinkedIn",
  //   ICON: "linkedin",
  //   TEXT: "markhorn-dev",
  //   HREF: "https://www.linkedin.com/in/markhorn-dev/",
  // },
  // { 
  //   NAME: "Twitter",
  //   ICON: "twitter-x",
  //   TEXT: "markhorn_dev",
  //   HREF: "https://twitter.com/markhorn_dev",
  // },
]

