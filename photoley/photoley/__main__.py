import argparse
import os
import sys

from . import config
from photoley.photos.photos import Photos
from photoley.configuration.configure import Configure


class Main(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            prog='photoley',
            description="Using unsplash, fetch random wallpaper with specific size and category.",
            epilog='Enjoy the Photoley',
            usage='''%(prog)s <command> [options]

Commands
--------
configure   Set and Update Configuration
photo       Using unsplash, fetch random wallpaper with specific size and category.'''
        )
        parser.add_argument('command', help='Subcommand to run')

        parser.add_argument('-v',
            '--version',
            help="Check version",
            action="version",
            version=f'%(prog)s {config.VERSION}'
        )

        args = parser.parse_args(sys.argv[1:2])

        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def configure(self):
        parser = argparse.ArgumentParser(
            description="Set and Update Configuration"
        )

        parser.add_argument('-c', '--channel',  metavar='', type=str, help="Set Desktop Screen channel")
        parser.add_argument('-p', '--property',  metavar='', type=str, help="Set Desktop Screen property")
        args = parser.parse_args(sys.argv[2:])

        return Configure(args).configure()

    def photo(self):
        parser = argparse.ArgumentParser(
            description="Using unsplash, fetch random wallpaper with specific size and category."
        )


        parser.add_argument('-q', '--query', metavar='', type=str, help="Comma-separated string search query to get relevant random image")
        parser.add_argument('-r', '--resolution', metavar='', type=str, help="Resolution of screen. eg: 1920x1080, 1366x768")
        parser.add_argument('-u', '--user', metavar='', type=str, help="Username that exists in unsplash eg: erondu")
        parser.add_argument('-c', '--collection', metavar='', type=int, help="Integer: Collection that exists in unsplash eg: 190727")
        parser.add_argument('-w', '--setwall', action="store_true", help="Set wallpaper for Desktop")

        args = parser.parse_args(sys.argv[2:])

        p = Photos(args=args, url=config.UNSPLASH_URL, dir=config.MEDIA_DIR)
        p.save()
