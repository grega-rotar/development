import type { Site, Page, Links, Socials } from "@types"

// Global
export const SITE: Site = {
  TITLE: "Grega Rotar",
  DESCRIPTION: "Welcome to Grega Rotar's portfilio",
  AUTHOR: "Grega Rotar",
}

// Work Page
export const JOURNEY: Page = {
  TITLE: "Journey",
  DESCRIPTION: "My working journey.",
}

// Projects Page 
export const PROJECTS: Page = {
  TITLE: "Projects",
  DESCRIPTION: "Recent projects I have worked on.",
}

// devHub Page 
export const DEV_HUB: Page = {
  TITLE: "Dev Hub",
  DESCRIPTION: "My dev things!",
}

// Connect page
export const CONNECT: Page = {
  TITLE: "Connect",
  DESCRIPTION: "Work with me!"
}

// Search Page
export const SEARCH: Page = {
  TITLE: "Search",
  DESCRIPTION: "Search all posts and projects by keyword.",
}

// Links
export const LINKS: Links = [
  // { 
  //   TEXT: "Home", 
  //   HREF: "/", 
  // },
  { 
    TEXT: "Journey", 
    HREF: "/journey", 
  },
  { 
    TEXT: "Projects", 
    HREF: "/projects", 
  },
  {
    TEXT: "Dev Hub",
    HREF: "/devHub"
  },
  {
    TEXT: "Connect",
    HREF: "/connect"
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
  { 
    NAME: "LinkedIn",
    ICON: "linkedin",
    TEXT: "grega-rotar-51103121b",
    HREF: "https://www.linkedin.com/in/grega-rotar-51103121b/",
  },
  { 
    NAME: "Twitter",
    ICON: "twitter-x",
    TEXT: "grega_rotar",
    HREF: "https://twitter.com/grega_rotar",
  },
]

